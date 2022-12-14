def morse(text="") -> str:
    """
    Program Untuk Menghasilkan kode morse dari text
    """
    pasw = ""
    key = {
        "A":".-",
        "B":"-...",
        "C":"-.-.",
        "D":"-..",
        "E":".",
        "F":"..-.",
        "G":"--.",
        "H":"....",
        "I":"..",
        "J":".---",
        "K":"-.-",
        "L":".-...",
        "M":"--",
        "N":"-.",
        "O":"---",
        "P":".--.",
        "Q":"--.-",
        "R":".-.",
        "S":"...",
        "T":"-",
        "U":"..-",
        "V":"...-",
        "W":".--",
        "X":"-..-",
        "Y":"-.--",
        "Z":"--..",
        " ":"/",
        "1":".----",
        "2":"..---",
        "3":"...--",
        "4":"....-",
        "5":".....",
        "6":"-....",
        "7":"--...",
        "8":"---..",
        "9":"----.",
        "0":"-----",
        ".":".-.-.-",
        ",":"--..--",
        "?":"..--..",
        "!":"-.-.--",
        "'":".----.",
        '"':".-..-.",
        "(":"-.--.",
        ")":"-.--.-",
        "&":".-...",
        ":":"---...",
        ";":"-.-.-.",
        "/":"-..-.",
        "_":"..--.-",
        "=":"-...-",
        "+":".-.-.",
        "-":"-....-",
        "$":"...-..-",
        "@":".--.-.",
    }
    try:
        for t in str(text):
            if t == " ":
                pasw += "/"
                continue
            pasw += key[t]+"/" 
        pasw += "/"
    except:
        print("ERROR")
    return pasw

pesan = input("Masukan Pesan : ").upper()
mypasw = morse(pesan)
print("sandi morse = \n"+mypasw)