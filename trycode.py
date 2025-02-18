names_tuple = 'Rod', 'Jane', 'Freddy'

# the TRY block attempts to run some code
# it prints the original tuple.
# it sorts the tuple into a list and appends "Bungle".
# it then tries to modify the tuple (which is not allowed).
# this causes a TypeError.
try:
    print("###### TRY #######")
    print("The TRY block attempts to run")
    print(f"Original Tuple: {names_tuple}")
    names_sorted_as_list = sorted(names_tuple)
    print(names_sorted_as_list)
    names_sorted_as_list.append("Bungle")
    print("Added Bungle:", names_sorted_as_list)
    print("Attempt to manipulate the tuple...")
    names_tuple[0] = 'Zippy'
    print("Is this code reached?")

# the EXCEPT blocks catch different types of errors
# FileNotFoundError: if a file-related issue occurs (not relevant here)
# TypeError: triggers when we try to change the tuple (this will happen!)
# Exception: a general pop up for unexpected errors
except FileNotFoundError as error:
    print("###### EXCEPT: FileNotFoundError #######")
    print("The EXCEPT / CATCH block only runs if this error happens")
    print(f"The following file can not be found: {error.filename}. Please try another file")

except TypeError as error:
    print("###### EXCEPT: TypeError #######")
    print("Oh dear, that is not allowed on that type")
    print(error)

except Exception as error:
    print("###### EXCEPT: Exception #######")
    print("Generic catch-all except / catch block")
    print(error)

# The FINALLY block always runs
# resets names_tuple to None to clean memory
finally:
    # Always close file handle after use
    print("The FINALLY block ALWAYS runs")
    print("The finally block is used to tidy up")
    if names_tuple:
        names_tuple = None

print("After exception handling is finished...the program can continue")
