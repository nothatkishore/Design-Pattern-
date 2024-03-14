class PurchaseRequest:
    def __init__(self, amount):
        self.amount = amount


class Approver:
    
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.next_approver = None
    
    def set_next_approver(self, next_approver):
        self.next_approver = next_approver
    
    def process_payment(self, request):
        if request.amount <= self.amount:
            print(f"{self.name} approved this {request.amount}")
        elif self.next_approver is not None:
            self.next_approver.process_payment(request)
        else:
            print("Request processing not possible")


if __name__ == "__main__":
    team_lead = Approver("Team Lead", 5000)
    manager = Approver("Manager", 10000)
    director = Approver("Director", 15000)

    team_lead.set_next_approver(manager)
    manager.set_next_approver(director)

    requests = [PurchaseRequest(1000), PurchaseRequest(6000), PurchaseRequest(12000), PurchaseRequest(20000)]
    
    for request in requests:
        team_lead.process_payment(request)
