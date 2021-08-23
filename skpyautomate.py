from skpy import Skype
import time
import os.path


#run this function when user is loggedIn
def allCommandsLoggedIn():
   with open('username.txt') as f:
       ulines = f.read()
       username = ulines

   with open('password.txt') as g:
       plines = g.read()
       password = plines

   sk = Skype(username, password)
   sk.user
   sk.contacts
   sk.chats
   print("Logged in as '",username, "'.")

   def sendMessageFunction():
      print("")
      commandInput = input("Enter command $/> ")

      if commandInput == 'send message' or commandInput == 'Send message' or commandInput == 'send Message' or commandInput == 'Send Message':
         
         user_id = input(" [1] Enter the ID of the user in skype:  ")
         enter_message = input(" [2] Enter message that you want to send:  ")
         time_limit = int(input(" [3] Enter time (when to send) in seconds:   "))

         print("  [4] Sending message after", time_limit, "seconds from now...")

         ch = sk.contacts[user_id].chat
         time.sleep(time_limit)
         ch.sendMsg(enter_message)

         print("  [5] Message successfully sent.")

      elif commandInput == '-help':
         print("  [1] Available commands:")
         print("  [2] Send Skype message - 'send message'")
         
      elif commandInput == '-exit':
         print("  Exiting...")
         time.sleep(4)
         print("  Successfully exited.")
      else:
         print("  [1] Incorrect command. Type '-help' to know more. ")
         
   for i in range(1000):
      sendMessageFunction()
      



#run this function when user is not loggedIn
def allCommandsNotLoggedIn():
   usernameu = str(input("Enter your skype email: "))
   passwordp = str(input("Enter your skype password: "))

   with open('username.txt', 'w+') as fp:
      write_username = fp.write(usernameu)
      new_username = write_username

   with open('password.txt', 'w+') as fp:
      write_password = fp.write(passwordp)
      new_password = write_password
   
   allCommandsLoggedIn()



#asking user if he/she has logged in before
print("SkpyAutomate [v1.0.0]")
      
if os.path.isfile('username.txt'):
   if os.path.isfile('password.txt'):
      allCommandsLoggedIn()
   else:
      print("  Sorry! An error occured")
            
else:
   allCommandsNotLoggedIn()


   


