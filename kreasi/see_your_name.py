# Ide ini saya dapatkan dari source code playground di solo learn
# Jadi ini bukan ide saya seutuhnya

pattern = {
    "a":"""
        __
       /  \ 
      /____\ 
     /      \ 
    /        \ """,
     "b":"""
      ____
     |    |
     |____/
     |    \ 
     |____|""",
     "c":"""
      ____
     /    
     |
     |
     \____ """,
     "d":"""
      ____
     |    \ 
     |     |
     |     |
     |____/ """,
     "e":"""
      ____
     |
     |____
     |
     |____""",
     "f":"""
      ____
     |
     |____
     |
     |    """,
     "g":"""
      ____
     /
     |  __
     |    \ 
     \____/ """,
     "h":"""
     |     |
     |_____|
     |     |
     |     |""",
     "i":"""
     _______
        |
        |
        |
     ___|___""",
     "j":"""
       _____
         |
         |
         |
     |   |
     \___/""",
     "k":"""
     |  /
     |_/
     | \ 
     |  \ """,
     "l":"""
     |
     |
     |
     |_____ """,
     "m":"""
      _       _
     | \     / |
     |  \   /  |
     |   \ /   |
     |         |""",
     "n":"""
      _
     | \    |
     |  \   |
     |   \  |
     |    \_|""",
     "o":"""
      _______
     /       \ 
     |       |
     |       |
     \_______/""",
     "p":"""
      _____
     |     \ 
     |_____/
     |
     |""",
     "q":"""
      ______
     /      \ 
     |      |
     |    \ |
     \_____\/
            \ """,
     "r":"""
      _____
     |     \ 
     |_____/
     |   \ 
     |    \ """,
     "s":"""
      ______
     /
     \______
            \ 
      ______/ """,
     "t":"""
     _________
         |
         |
         |
         |""",
     "u":"""
     |     |
     |     |
     |     |
     \_____/ """,
     "v":"""
     \       /
      \     /
       \   /
        \_/ """,
     "w":"""
     \          /
      \        /
       \  /\  /
        \/  \/ """,
     "x":"""
     \   /
      \ /
      / \ 
     /   \ """,
     "y":"""
      \   /
       \_/
        | 
        | """,
     "z":"""
     _______
          /
         /
        /
       /
      /______"""
}

# [print(pattern[i]) for i in pattern]

name = input("Masukan Nama : ")
words = name.lower()
for word in words:
    print(pattern[word])