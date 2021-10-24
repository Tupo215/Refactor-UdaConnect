import grpc
import person_id_pb2
import person_id_pb2_grpc

channel = grpc.insecure_channel("localhost:5005")
stub = person_id_pb2_grpc.PesronIDServiceStub(channel)

# Enter person Id
person_id = input("Enter person_id:")
id = int(person_id) # Turn person ID into interger

# This is a if else funtion to filter througn the avaible id's and return 
# the person id, first name, last name and company if none of the id's match 
# an error will be given

if id == 1:
    response = stub.GetID(person_id_pb2.PersonIDMessage(
        id = 1,
        first_name = "Pam",
        last_name = "Trexler",
        company_name = "Hampton, Hampton and McQuill"))
    print(response)

elif id == 5:
    response = stub.GetID(person_id_pb2.PersonIDMessage(
        id = 5,
        first_name = "Taco",
        last_name = "Fargo",
        company_name = "Alpha Omega Upholstery"))
    print(response)

elif id == 6:
    response = stub.GetID(person_id_pb2.PersonIDMessage(
        id = 6,
        first_name = "Frank",
        last_name = "Shader",
        company_name = "USDA"))
    print(response)

elif id == 8:
    response = stub.GetID(person_id_pb2.PersonIDMessage(
        id = 8,
        first_name = "Paul",
        last_name = "Badman",
        company_name = "Paul Badman & Associates"))
    print(response)

elif id == 9:
    response = stub.GetID(person_id_pb2.PersonIDMessage(
        id = 9,
        first_name = "Otto",
        last_name = "Spring",
        company_name = "The Chicken Sisters Restaurant"))
    print(response)
                
else:
    print('Error: No such person ID')