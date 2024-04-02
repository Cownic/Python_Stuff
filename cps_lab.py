def hex_to_ascii(hex_value):
  """
  Converts a hexadecimal string to its corresponding ASCII character(s).

  Args:
      hex_value: A string containing the hexadecimal value.

  Returns:
      A string containing the ASCII character(s) represented by the hexadecimal value.
  """
  try:
    # Convert the hexadecimal string to an integer (base 16)
    int_value = int(hex_value, 16)
    
    # Ensure the integer value is within the valid ASCII range (0-127)
    if 0 <= int_value <= 127:
      # Convert the integer value to its ASCII character
      return chr(int_value)
    else:
      # Handle invalid values outside the ASCII range
      print(f"Warning: Hex value '{hex_value}' is outside the ASCII range (0-127).")
      return ""
  except ValueError:
    # Handle invalid input that cannot be converted to integer
    print(f"Error: Invalid hexadecimal value '{hex_value}'.")
    return ""

def main():
    response = "01 FF FF 38 34 9F 76 B4 49 4E 47 45 4E 49 20 00 30 FF FF 38 34 62 D6 3E 41 44 4D 2D 50 4E 52 20 76 00 00 28 34 48 CA E8 42 55 53 31 39 39 20 00 31 FF FF 65 34 48 C6 DF 42 55 53 31 39 39 20 00 31 FF FF A1 34 48 AB 4A 42 55 53 31 37 39 20 00 30 FF FF 65 33 F2 49 20 43 43 4B 2D 41 44 4D 20 30 FF FF 3B 33 F0 7B 15 42 4E 4C 2D 41 44 4D 20 31 FF FF 8D 33 F0 53 9D 42 55 53 20 31 37 39 00 76 00 00 06 33 F0 1C 6C 42 55 53 20 31 37 39 00 31 FF FF F1 33 F0 16 90 42 55 53 20 31 37 39 00 30 FF FF 6D 33 F0 15 F9 41 44 4D 2D 42 4E 4C 20 76 00 00 02 33 EF 92 A9 42 55 53 20 39 31 33 00 31 FF FF F8 33 EF 91 1F 42 55 53 20 39 31 33 00 30 FF FF 3E 33 EF 90 56 50 4E 52 2D 57 44 4C 20 76 00 00 06 33 EF 29 FF 42 55 53 31 37 39 20 00"
    response_split = response.split()
    hex_integers = [int(x, 16) for x in response_split]

    list_of_transactions = []
    size_of_each_transaction = 16

    for i in range(0, len(hex_integers), size_of_each_transaction):
      transaction_now = hex_integers[i: i+size_of_each_transaction]
      list_of_transactions.append(transaction_now)

    for transaction in list_of_transactions:
      transaction_user_data = transaction[-8:]
      transaction_user_data_string = [chr(i) for i in transaction_user_data]
      print("My transaction user data for this log is {}".format(transaction_user_data_string))

    # byte16_array = []
    # start = 0
    # size = len(response_split)
    # while start <= size:
    #     byte16_array.append(response_split[start:start+16])
    #     start += 16

    # log = []
    # for i in range(len(byte16_array)):
    #     # Trasaction User Data
    #     result_user_data = byte16_array[i][-8:]
    #     string_result_user_data = ''.join(result_user_data)
    #     bytes_values = bytes.fromhex(string_result_user_data)
    #     ascii_string = bytes_values.decode("ASCII")
    #     # Transaction Amount
    #     result_trans_amount = byte16_array[i][-15:-12]
    #     string_result_trans_amount = ''.join(result_trans_amount)
    #     bytes_value = bytes.fromhex(string_result_trans_amount)
    #     decimal_value = int.from_bytes(bytes_value, byteorder='big', signed=True)

    #     print("Log " + str(i) + " Purpose: " + ascii_string + " Cost: " + str(decimal_value/100))
    #     print("__________________________________")

if __name__=="__main__":
   main()

