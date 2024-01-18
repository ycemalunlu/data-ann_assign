file_path = 'coding_qual_input.txt'
message_file = open(file_path, 'r')
       

def decode(message_file):
    
    # Since we can't check longer text files manually,
    # making sure that we are getting the highest number instead of getting number of rows.
    # Because there it is not indicated that the data is already checked.
    def get_max(lines):
        return max(int(line.split()[0]) for line in lines)    
    
    # After getting the highest number this method is creating a list of
    # numbers which are the last numbers on each row in the pyramid
    def get_row_values(length):
        nums = [*range(1, length + 1)]
        step = 1
        subsets = []
        while len(nums) != 0:
            if len(nums) >= step:
                subsets.append(nums[step-1])
                nums = nums[step:]
                step += 1
            else:
                break
        return subsets    


    #Creating a dictionary for numbers and corresponding values
    def num_to_word_dict(lines):
        number_to_word = {}
        for line in lines:
            parts = line.split()
            number_to_word[int(parts[0])] = ' '.join(parts[1:])
        return number_to_word
        
   
    lines = message_file.readlines()
    number_to_word = num_to_word_dict(lines)
    max_value = get_max(lines)
    row_values = get_row_values(max_value)
    corresponding_words = [number_to_word[number] for number in row_values if number in number_to_word]
    result_string = ' '.join(corresponding_words).lower()
    message_file.close()
    
    return result_string


print(decode(message_file))





# get_max(lines): Created this method to be able to find the word with the highest corresponding value. Couldn't be sure that we can trust the number of rows since there is no information about it.

# get_row_values(length): Edited the staircase method which was a part of a question above in the assignment to get a list of the only the last values of the each row in the pyramid.

# num_to_word_dict(lines): Wrote this to create a dictionary to use in decoding process which is taking numbers as keys and returning the corresponding words.

# used these methods to create a list of the corresponding_words and converted this list into a string formatted to meet requirements of the assignment

