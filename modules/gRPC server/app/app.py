import time
from concurrent import futures
import grpc
import person_id_pb2
import person_id_pb2_grpc

class PersonIDServicer(person_id_pb2_grpc.PesronIDServiceServicer):
    def GetID(self, request, context):
        result = person_id_pb2.PersonIDMessage(
            id = request.id,
            first_name = request.first_name,
            last_name = request.last_name,
            company_name = request.company_name)
        
        return result
        
	    
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
person_id_pb2_grpc.add_PesronIDServiceServicer_to_server(PersonIDServicer(), server)


# Server starting on port 5005
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)