def response(input_message):
    message = input_message.lower()
    a  = message.split()
    

    if message == 'nice':
         print('very nice')
         return 'very nice'
    elif (message == 'tq') or (message=='thanks'):
         print("it's ok, but i usually don't take tqs")
    elif (message == 'hlo') or (message=='hello') or (message=='hy') or (message=='hyy') or (message=='hi')or (message=='hiii')or (message=='hii') or (message == 'Helloo'):
         print("HELLO THERE how r u")
         return "HELLO THERE how r u"
    elif (message == 'what about u???') or (message == 'what about you???') or (message == 'what about you??') or (message == 'what about you?') or (message == 'what about you') or (message == 'what about u??') or (message == 'what about u?') or (message == 'what about u') or (message == 'how are u???') or  (message == 'how are u??') or (message == 'how are u') or (message == 'how are you??')or (message == 'how are you???')or (message == 'how are you?')or (message == 'how are you') :
         print("I am fine as well")
         return "I am fine as well"  
    elif 'ok' in a:

         print("ok boss")
         return 'ok boss'
    else:
         print("my boss is not here he will talk to you later")
         return "my boss is not here he will talk to you later"

