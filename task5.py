good = r"""               _.  
            ;=',_  
           S" .--` 
          sS  \__  
       __.' ( \--> 
    _=/    _./-\/  
   ((\( /-'   -'l  
    ) |/ \\    
  snd  \\  \ 
        `~ `~
"""
bad = r"""                     __       __
                     '.'--.--'.-'
       .,_------.___,   \' r'
       ', '-._a      '-' .'
        '.    '-'Y \._  /
          '--;____'--.'-,
       snd /..'       '''
"""
escaped = True
if escaped:
    outcome = "Legend: You did it, you are a hero who survived this adventure."
    print(good)
else:
    outcome = "Doom: Well you are still stuck, and you are probably dead soon."
    print(bad)
print(outcome)