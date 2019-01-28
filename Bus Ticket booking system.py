from random import randint


def check_source(object1):
    if (object1 in stations):
        return
    else:
        print('We do not have service in this city.')
        exit()

def check_dest_city(object2):
    if(object2 in stations):
        return
    else:
        print('We do not have service in this city.')
        exit()

print('\t\t*****Welcome to RSRTC Bus Service*****')
stations = ['BIKANER','KOTA','JAIPUR','CHURU','BHILWARA']
fare_chart={'BIKANER to KOTA':400,'BIKANER to JAIPUR':400,'BIKANER to CHURU':400,'BIKANER to BHILWARA':400,
            'KOTA to BIKANER':500,'KOTA to JAIPUR':500,'KOTA to CHURU':500,'KOTA to BHILWARA':500,
            'JAIPUR to BIKANER':350,'JAIPUR to KOTA':350,'JAIPUR to CHURU':350,'JAIPUR to BHILWARA':350,
            'CHURU to BIKANER':450,'CHURU to KOTA':450,'CHURU to JAIPUR':450,'CHURU to BHILWARA':450,
            'BHILWARA to BIKANER':600,'BHILWARA to KOTA':600,'BHILWARA to JAIPUR':600,'BHILWARA to CHURU':600}
Bus_timing={'BIKANER':6.00,'KOTA':6.15,'JAIPUR':7.00,'CHURU':8.00,'BHILWARA':10.00}
seat = 50
def search_bus():
    print('\n*****')
    print('\nWe Have Bus Service for these Cities :')
    for i in stations:
        print(i)
    source = input('\nFrom: ')
    source=source.upper()
    check_source(source)
    destination = input('\nTo: ')
    destination=destination.upper()

    check_dest_city(destination)
    journey_route = source+' to '+destination
    def Bus_details():
        print('\nBus Details for your route is: ')
        print('From: \t',source,'\t\tTo: \t',destination)
        print('Departure Time is: ',Bus_timing[source],'P.M.')
        print('Total Fare per seat is: ',fare_chart[journey_route])
        print('Available Seat is: ',seat)
    Bus_details()
    choice2 = input('\n\nDo You Want to Book a Ticket Y/N: ')
    choice2=choice2.upper()
    if(choice2=='Y'):
        book_ticket()
    else:
        exit()

def book_ticket():
    print('\n*****Welcome to RSRTC Ticket Booking Window*****')
    source1=input('\nFrom:  ')
    source1=source1.upper()
    check_source(source1)

    destination1=input('\nTo : ')
    destination1=destination1.upper()
    check_dest_city(destination1)
    journey_route1=source1+' to '+destination1
    journey_route = ('From: ')+source1+'\tTo: '+destination1
    journey_date=input('Enter Journey Date: ')

    seat=int(input('Choose a seat no. : '))
    def check_seat(x):
        if(x<1 or x>50):
            print('Please select a valid seat no. :')
            exit()
        else:
            return
    check_seat(seat)

    Pname = input('Enter Passenger Name: ')
    Pname.upper()
    def check_name(x):
        if(len(x)<=2):
            print('Enter a valid name:')
            exit()
        else:
            return
    check_name(Pname)

    Page=int(input('Enter Passenger Age: '))
    def check_age(x):
        if(x<12):
            print('Passenger age should be between 12 to 70.')
            exit()
        else:
            return
    check_age(Page)
    Pgender = input('Enter Passenger Gender Male/Female: ')
    Pgender.upper()
    Pno = input('Enter Contact detail: ')
    def check_no(x):
        if(len(x)!=10):
            print('Mobile No. is Invalid.')
            exit()
        else:
            return
    check_no(Pno)
    pnr=randint(293843,849372)
    print('\n\n**Ticket details**')
    print('\n',journey_route)
    print('PNR NO. : ',pnr)
    print('Name: ',Pname,'\t\t\t','Date: ',journey_date)
    print('Age: ',Page,'\t\t\t','Seat No. : ',seat)
    print('Gender: ',Pgender,'\t\t\t','Fare: ',fare_chart[journey_route1])
    print('Contact No. : ',Pno,'\t\t','Dept. Time: ',Bus_timing[source1],'P.M.')


def ticket_status():
    print('Sorry this service is temproraly Unavlable:')

print('1. Search Bus')
print('2. Book Ticket')
print('3. Search Ticket Status')

choice = int(input('Enter your choice: '))
if(choice==1):
    search_bus()
elif(choice==2):
    book_ticket()
elif(choice==3):
    ticket_status()
else:
    print('please choose a valid option ')
p = input()