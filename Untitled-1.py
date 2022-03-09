print('''
 _____    ____  __ ______________     ____   _____   ____ |  |___/  |______   
\__  \  /    \|  |  \_  __ \__  \   / ___\ /     \_/ __ \|  |  \   __\__  \  
 / __ \|   |  \  |  /|  | \// __ \_/ /_/  >  Y Y  \  ___/|   Y  \  |  / __ \_
(____  /___|  /____/ |__|  (____  /\___  /|__|_|  /\___  >___|  /__| (____  /
     \/     \/                  \//_____/       \/     \/     \/          \/ 
      ''')
with open("website.log","r") as f:
    lines=f.readlines()
    with open("output.txt", "w+") as nf:
        for line in lines:
          line=line.split()
          nf.write("ip:{} time:{} method:{} path:{} protocol:{} status code:{} packet size:{} user agent:{}".format(line[0],line[3:5],line[5],line[6],line[7],line[8],line[9],line[11:]))
           #print(f"IP : {line[0]}\t Time : {line[3]} \tMethod : {str(line[5]).replace('"',' '))}\tpath:{line[6]}\t http protocol:{line[7]}\tstatus code:{line[8]}\tpacket size:{line[9]}\tuser Agent:{line[11]}")