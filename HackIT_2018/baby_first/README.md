## Baby_first writeup  

Let's start by looking at what kind of file we have to reverse.  
  
```
$ file ./re1  
re1: ELF 64-bit LSB executable, ARM aarch64, version 1 (SYSV), statically linked, for GNU/Linux 3.7.0, BuildID[sha1]=48e70b04d5fdfcaccb8442dda6fec030f0f6b822, stripped  
```   
It looks like we have a 64bit arm stripped binary. Time to look for some interesting strings.  

```
$ strings -n 10 ./re1  
7&`@9D`@9E
7&`@9D`@9E
bk`8!k`8"k 8ak 8
(hf8'he8&hc8c>L
wat do u want? 
oh noes! you no haz flag!
yes, u got it! submit!
libc-start.c
__ehdr_start.e_phentsize == sizeof *GL(dl_phdr)
FATAL: kernel too old
...
```  
As we can see there are some tipical strings of a crackme challenge type (correct/wrong). Time to open up our disassembler.  
By giving a quick glimpse to the graph view we can clearly see a pattern in the first part of the code which can makes us think to a for loop and in the second block from the top if we end up cycling we reach the "Congratulation" message.  
This means that in the following code there will be a certain condition which will prevent us from ending all the nested cycles.

![Flow1](https://image.ibb.co/fYsj9p/2018_09_11_121211_1366x768_scrot.png)

In this second image we instead notice how it ends up a few more times with the previous pattern and then it starts performing some dense operations.

![Flow2](https://image.ibb.co/hceZaU/2018_09_11_121224_1366x768_scrot.png)  

I will not go into much details in reversing the calculation part cause it's pretty boring, if you are interested have a look at solve.py script where I defined all the reversed constrains for Z3 and let him perform the magic.  
  
To have a general idea the program takes values from a certain memory area based on the characters of the password provided by the user and the current values of the indexes of the nested for loops and performs additions and multiplications between those values saving the value in a variable which I called SUM.  
Immediately after the end of the most inner loop this variable is compared to the expected result for the current "round" and if the comparison doesn't match the program exits with a failure message. Our goal is of course to be able to pass all the checks providing a valid input.
