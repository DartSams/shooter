import os
 
# Function to rename multiple files
def main(folder_num,title):
   
    folder = f"ghost-pack/PNG/Wraith_0{folder_num}/PNG Sequences/{title}"
    print(os.listdir(folder))
    num = 0
    for  filename in os.listdir(folder):
        dst = f"Wraith_0{folder_num}_{title}_{str(num)}.png"
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{dst}"
        
        # rename() function will
        # rename all the files
        os.rename(src, dst)
        num += 1
 
# Driver Code
if __name__ == '__main__':
     
    # Calling main() function
    # main()
    lst = ["Dying","Idle"] #folders to go into and rename files
    for i in range(1,4): #cycle through 3 folders starting at 1
        for j in lst: #cyle through folder names
            main(i,j)