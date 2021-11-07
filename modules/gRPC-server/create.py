import grpc
import create_locations_pb2
import create_locations_pb2_grpc

# Connect to gRPC server running on 30003

channel = grpc.insecure_channel("localhost:30003")
stub = create_locations_pb2_grpc.LocationServiceStub(channel)

# Use this to test the gRPC server to create a new user

response = stub.Create(create_locations_pb2.LocationMessage(
        id = 69,
        person_id = 1,
        creation_time = "2021-11-06 11:57:06.000000",
        coordinate = "kberyaosnejoisdhand"))
print(response)