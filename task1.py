good = r"""                    .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
          snd                         (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-'
"""

bad = r"""                            __
     ,                    ," e`--o
    ((                   (  | __,'
     \\~----------------' \_;/
hjw  (                      /
     /) ._______________.  )
    (( (               (( (
     ``-'               ``-'
"""
torch_lit = True
if torch_lit:
    outcome = "Flicker: You start walking, because you can see."
    print(good)
else:
    outcome = "Doom: You're cooked, and blind."
    print(bad)
print(outcome)