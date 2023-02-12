import subprocess

# fingerprinting...

print_output = ""

for ping in range(1,256): 
    # build a dynamic IP address string using the incrementing value in the for loop (number)
    address = "172.16.0." + str(ping)

    # NEXT LINE MAY DIFFER DUE TO OS: - win64
    # ping is a computer network administration software utility used to test the 
    # reachability of a host on an Internet Protocol (IP) network.
    # https://en.wikipedia.org/wiki/Ping_(networking_utility)
    output = subprocess.Popen(["ping.exe",address],stdout = subprocess.PIPE).communicate()[0]

    if str(output).find("unreachable") == -1:
        print_output += "{} is ONLINE!\n".format(address)
        print(address,"--------------------------------")
        print(output)
        print("--------------------------------")        
    else:
        print_output += "{} is offline\n".format(address)

print(print_output)
