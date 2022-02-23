import sshtunnel

def connectToServer(serverName, portNumber):
    tunnel = sshtunnel.SSHTunnelForwarder(ssh_address_or_host= serverName, remote_bind_address=('localhost', portNumber))
    tunnel.start()
    return tunnel

def closeServerConnectivity(tunnel):
    tunnel.close()
