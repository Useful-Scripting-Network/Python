'''
    Class to check if port connection is open or not. 
    
    Author: Clayton E.
'''
import socket, time, logging, platform, getpass, os
from colorama import init, Fore
from requests import get

# Setup colorama
init()

# Define internet connection
def tryinternet(host="8.8.8.8", port=53, timeout=3):
  """
  Host: 8.8.8.8 (google-public-dns-a.google.com)
  OpenPort: 53/tcp
  Service: domain (DNS/TCP)
  """
  try:
    socket.setdefaulttimeout(timeout)
    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
    return True
  except socket.error as ex:
    print(ex)
    return False


# Setup logging
file, ext = os.path.splitext(__file__)
logfile = file+'.log'
logging.basicConfig(filename=logfile, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO, datefmt='%b-%d-%y %H:%M:%S')

# Check if we have internet first
if tryinternet():
    print('Connected to internet')
else:
    print('Ensure you have a connection to the internet...')
    logging.error('No internet connection')
    print('Closing in 10 seconds...')
    time.sleep(10)
    os._exit(0)
    
# Get basic system information
system = platform.system()
release = platform.release()
version = platform.version()
currentuser = getpass.getuser()
host_name = socket.gethostname() 
host_ip = socket.gethostbyname(host_name) 
exipaddress = get('https://ipapi.co/ip/').text

logging.info('Beginning System Check')
logging.info(f'Operating System: {system} {release}')
logging.info(f'Current user: {currentuser}')
logging.info(f'Hostname: {host_name}')
logging.info(f'Local IP: {host_ip}')
logging.info(f'External IP: {exipaddress}')
logging.info('Beginning Port Check')

# header used to print and log the section we are checking if checking multiple types of connections
def header(title):
    print(' ')
    print(title)
    logging.info(title)
    print('-' * 30)


# Setup the class
class PortCheck:
    def __init__(self, domain, port):
        self.domain = domain
        self.port = port
        self.retry = 1
        self.delay = 5
        self.timeout = 3


    def isOpen(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(self.timeout)
        try:
            s.connect((self.domain, int(self.port)))
            s.shutdown(socket.SHUT_RDWR)
            return True
        except:
            return False
        finally:
            s.close()


    def checkHost(self):
        ipup = False
        for i in range(self.retry):
            if self.isOpen():
                ipup = True
                break
            else:
                time.sleep(self.delay)
        return ipup
    
    
    def portReturn(self):
        if self.checkHost():
            print(f"{self.domain}:{self.port} is {Fore.GREEN} OPEN {Fore.RESET}")
            logging.info(f"{self.domain}:{self.port} is OPEN")
        else:
            print(f"{Fore.RED}{self.domain}:{self.port} is CLOSED {Fore.RESET}")
            logging.error(f"{self.domain}:{self.port} is CLOSED")


if __name__ == "__main__":
    # Setup URLs and ports
    google = PortCheck("google.com", 443)
    facebook = PortCheck("facebook.com", 443)
    usefulscriptingnetwork = PortCheck("usefulscripting.network", 80)
    localhost = PortCheck("localhost", 445)
    badhost = PortCheck("usefulscripting.network", 4000)


    ###########################################################
    ###                                                     ###
    ###         Begin checking the connections here         ###
    ###                                                     ###
    ###########################################################


    # Check our hosts
    header("Checking Hosts")
    google.portReturn()
    facebook.portReturn()
    usefulscriptingnetwork.portReturn()
    localhost.portReturn()
    badhost.portReturn()

    # Close out prompt window
    print('\n')
    print(f"Log file: {logfile}")
    print("Press Enter to continue ...")
    input()
