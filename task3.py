good = r"""                .=.A.=.
          __.=./\ / \ /\.=.__
         (-.'-;  |   |  ;-'.-)
            \ `\/     \/` /
             ;  `\   /`  ;
             |    | |    |
             ;,"-.-"-.-",;
              \\/^\ /^\//
               \   `   /
           jgs  ',___,'
                 \\V//
                  |||
                  |||
                  |||
"""
bad = r"""            ____
        _.-'78o `"`--._
    ,o888o.  .o888o,   ''-.
  ,88888P  `78888P..______.]
 /_..__..----""        __.'
 `-._       /""| _..-''
     "`-----\  `\
             |   ;.-""--..
             | ,8o.  o88. `.
             `;888P  `788P  :
       .o""-.|`-._         ./
      J88 _.-/    ";"-P----'
      `--'\`|     /  /
          | /     |  |
          \|     /   |akn
           `-----`---'
"""
guard_awake = True
if not guard_awake:
    outcome = "Shadow: Fantastic, the guard is sleeping and you can sneak past."
    print(good)
else:
    outcome = "Doom: The guard catches you, and you are given a death sentence."
    print(bad)
print(outcome)