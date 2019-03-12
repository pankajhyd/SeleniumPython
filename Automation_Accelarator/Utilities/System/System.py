import socket
import getpass

'''
Function Name           : fnHotsName
Function Creation Date  : 18-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Get Host Name
'''
def fnHotsName():
    return socket.gethostname();


'''
Function Name           : fnGetUserName
Function Creation Date  : 18-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Get User Name
'''
def fnGetUserName():
    return getpass.getuser();