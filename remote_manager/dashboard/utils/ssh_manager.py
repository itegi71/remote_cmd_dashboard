import paramiko  

class SSHClientManager:
    """
    class to manage SSH connections using paramiko
    """
    def __init__(self,hostname,port,username,password):
        self.hostname=hostname
        self.port=port
        self.username=username
        self.password=password
        self.client=None

    def connect(self):

        #establish an ssh connecction
        try:
            self.client=paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(
                hostname=self.hostname,
                port=self.port,
                username=self.username,
                password=self.password
            )
        except Exception as e:
            raise ConnectionError(f"failed to connect:{e}")
        

        def execute_command(self,command):
            """
            run a command on the remote server
            """
            if not self.client:
                raise ConnectionError("SSH Connection not established")
            
            stdin,stdout,stderr=self.client.exec_command(command)
            output=stdout.read().decode()
            error=stderr.read().decode()
            return output if output else error
        
        def close(self):
            """
            close the SSH connection
            """
            if self.client:
                self.client.close()


    
    


        


                
