import base64

def encode_data_to_base64(data):

    coded_data = []

    for line in data:

        line_bytes = line.encode("utf-8")
    
        line64_bytes = base64.b64encode(line_bytes)
    
        base64_line = line64_bytes.decode("utf-8")

        coded_data.append(base64_line)

    return coded_data