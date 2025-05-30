import socket
import signal
from .connection_manager import ConnectionManager

def start_protection_server(config, port=None):
    """Start the DDoS protection server"""
    port = port or config['default_port']
    manager = ConnectionManager(config)
    
    def handle_shutdown(signum, frame):
        manager.log("Shutdown signal received")
        manager.shutdown()
        raise SystemExit
    
    signal.signal(signal.SIGINT, handle_shutdown)
    signal.signal(signal.SIGTERM, handle_shutdown)
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            if os.name == 'nt':
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            sock.bind((config['protected_ip'], port))
            sock.listen(config['backlog'])
            
            manager.log(f"Server started on {config['protected_ip']}:{port}")
            
            while manager.running:
                try:
                    conn, addr = sock.accept()
                    threading.Thread(
                        target=manager.handle_connection,
                        args=(conn, addr),
                        daemon=True
                    ).start()
                except OSError:
                    if not manager.running:
                        break
                    raise
                    
    except Exception as e:
        manager.log(f"Server error: {e}")
    finally:
        manager.shutdown()