import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
 
number=0
def main():
 recognizer = aiy.cloudspeech.get_recognizer()
 recognizer.expect_phrase('The number is 1.')
 recognizer.expect_phrase('The number is 2.')
 recognizer.expect_phrase('The number is 3.')
 recognizer.expect_phrase('What is the number?')


aiy.audio.get_recorder().start()
 
while True:
 print('Press the button and speak')
 button.wait_for_press()
 print('Listening...')
 text = recognizer.recognize()
 if not text:
  print('Sorry, I did not hear you.')
  else:
    print('You said "', text, '"')
     if 'The number is 1.' in text:
      number = 1
     elif 'The number is 2.' in text:
      number = 2
     elif 'The number is 3.' in text:
      number = 3
     elif 'goodbye' in text
      print('The number is "'number '"')
      break
 
 
if __name__ == '__main__':
 main()