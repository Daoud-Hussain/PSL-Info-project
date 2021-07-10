print("-----------------------")
print("Signup for free!")
print("_________")
username= input("\nEnter Your UserName: ")
email= input("Enter your Email Address: ")
password = int(input("Enter your password: "))
if "gmail.com" in email:
 if '@' in email:
    i = 0
    while True: 
        print('''
            __________
            ** Topic: HBL PSL)**
            1. Players
            2. Teams
            3. Team staff
            4. Ticket Reservation
            5. Exit
            __________''')
        action = int(input("Enter your choice: "))
        if action == 1:
            print("Which players of team you want: ")
            print('''
            __________
            ** Teams **
            1. Islamabad United
            2. Karachi Kings
            3. Lahore Qalandars
            4. Multan Sultan
            5. Peshawar Zalmi
            6. Quetta Gladiators
            7. Exit
            ----------------------------''')
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print('''
            __________
            ** Squad ***
            1. Shadab Khan (C)
            2. Hasan Ali (VC)
            3. Rohail NAzeer (WK)
            4. Faheem Ashraf 
            5. Asif Ali 
            6. Hussain Talat 
            7. Janeman Malan 
            8. Fawad Ahmed
            9. Musa Khan
            10.Akif Javed
            11.Andre Fletcher 
            __________''')
                player = int(input("Enter player number: "))
                if player == 1:
                    print('''
                __________
                ** Players **
                Name: Shadab Khan
                Country: Pakistan
                Age: 24
                Specification: Bowling All-rounder
                Batsman: Right-Handed Batsman
                Bowler: Right Arm Orthodax
                __________''' )
                elif player == 2:
                    print('''
                __________
                ** Players **
                Name: Hasan Ali
                Country: Pakistan
                Age: 25
                Specification: Bowler
                Style: Right-Arm Fast
                __________''' )
                elif player == 3:
                    print('''
                __________
                Name: Rohail Nazeer
                Country: Pakistan
                Age: 22
                Specification: Wicketkeeper Batsman
                Batting style: Right-Handed Batsman
                __________''' )
                elif player == 4:
                    print('''
                Name: Faheem Ashraf
                Country: Pakistan
                Age: 26
                Specification: Batting All Rounder
                __________''' )
                elif player == 5:
                    print('''
                Name: Asif Ali
                Country: Pakistan
                Age: 29
                Specification: Batsaman''' )
                elif player == 6:
                    print('''
                Name: Hussain Talat
                Country: Pakistan
                Age: 23
                Specification: Batting All-Rounder''' )
                elif player == 7:
                    print('''
                Name: Janeman Malan
                Country: South Africa
                Age: 27
                Specification: Batsman''' )
                elif player == 8:
                    print('''
                Name: Fawad Ahmed
                Country: Australia
                Age: 29
                Specification: Spin Bowler''' )
                elif player == 9:
                    print('''
                Name: Musa Khan
                Country: Pakistan
                Age: 20
                Specification: Fast Bowler''' )
                elif player == 10:
                    print('''
                Name: Akif Javed
                Country: Pakistan
                Age: 24
                Specification: Fast Bowler''' )
                elif player == 11:
                    print('''
                Name: Andre Fletcher
                Country: West Indies
                Age: 29
                Specification: Batsaman''' )
            elif choice == 2:
                print('''
            1. Imad Waseem (C)
            2. Babar Azam (VC)
            3. Chadwic Walton (WK)
            4. Sharjeel Khan
            5. Martin Guptil
            6. M Amir 
            7. Arshad Iqbal
            8. Waqas Maqsood
            9. Aamir Yamin
            10. Danish Aziz
            11. Qasim Akram
            __________''')
                player = int(input("Enter player number: "))
                if player == 1:
                    print('''
                __________
                ** Players **
                Name: Imad Waseem
                Country: Pakistan
                Age: 27
                Specification: Bowling All-rounder
                Batsman: Left-Handed Batsman
                Bowler: Left Arm Offspin
                __________''' )
                elif player == 2:
                    print('''
                __________
                ** Players **
                Name: Babar Azam
                Country: Pakistan
                Age: 25
                Specification: Batsman
                Style: Right-Handed
                __________''' )
                elif player == 3:
                    print('''
                __________
                Name: Chadwick Walton
                Country: West Indies
                Age: 27
                Specification: Wicketkeeper Batsman
                Batting style: Right-Handed Batsman
                __________''' )
                elif player == 4:
                    print('''
                Name: Sharjeel Khan
                Country: Pakistan
                Age: 28
                Specification: Batsman
                __________''' )
                elif player == 5:
                    print('''
                Name: Martin Guptil
                Country: New Zealand
                Age: 29
                Specification: Batsaman''' )
                elif player == 6:
                    print('''
                Name: M Amir
                Country: Pakistan
                Age: 29
                Specification: Bowler''' )
                elif player == 7:
                    print('''
                Name: Arshad Iqbal
                Country: Pakistan
                Age: 21
                Specification: Bowlwer''' )
                elif player == 8:
                    print('''
                Name: Waqas MAqssod
                Country: Pakistan
                Age: 23
                Specification: FAst Bowler''' )
                elif player == 9:
                    print('''
                Name: Amir Yamin
                Country: Pakistan
                Age: 24
                Specification: Fast Bowler All-rounder''' )
                elif player == 10:
                    print('''
                Name: Danish Aziz
                Country: Pakistan
                Age: 22
                Specification: Bowling All-rounder''' )
                elif player == 11:
                    print('''
                Name: Qasim Akram
                Country: Pakistan
                Age: 21
                Specification: Batting All-rounder''' )
      
            elif choice == 3:
                print('''
            1. Sohail Akhtar (C)
            2. Shaheen Afridi (VC)
            3. Ben Dunk (WK)
            4. Ahmed Danial
            5. Maaz Khan
            6. Rashid Khan
            7. Haris Rauf
            8. Samit Patel
            9. M HAfeez
            10. FAkhar Zamnan
            11. David Wiese
            _________''')
                player = int(input("Enter player number: "))
                if player == 1:
                    print('''
                __________
                ** Players **
                Name: Sohail Akhtar
                Country: Pakistan
                Age: 24
                Specification: Batsman
                Batsman: Right-Handed Batsman
                __________''' )
                elif player == 2:
                    print('''
                __________
                ** Players **
                Name: Shaheen Afridi
                Country: Pakistan
                Age: 24
                Specification: Bowler
                Style: Left-Arm Fast
                __________''' )
                elif player == 3:
                    print('''
                __________
                Name: Ben Dunk
                Country: Austalia
                Age: 29
                Specification: Wicketkeeper Batsman
                Batting style: Left-Handed Batsman
                __________''' )
                elif player == 4:
                    print('''
                Name: Ahmed Danial
                Country: Pakistan
                Age: 21
                Specification: FAst Bowler
                __________''' )
                elif player == 5:
                    print('''
                Name: Maaz Khan
                Country: Pakistan
                Age: 23
                Specification: Spin Bowler''' )
                elif player == 6:
                    print('''
                Name: Rashid Khan
                Country: Afghanistan
                Age: 23
                Specification: Spin Bowler''' )
                elif player == 7:
                    print('''
                Name: Haris Rauf
                Country: Pakistan
                Age: 27
                Specification: Fast Bowler''' )
                elif player == 8:
                    print('''
                Name: Samit Patel
                Country: England
                Age: 32
                Specification: Spin Bowling All-Rounder''' )
                elif player == 9:
                    print('''
                Name: M HAfeez
                Country: Pakistan
                Age: 40
                Specification: Batsman''' )
                elif player == 10:
                    print('''
                Name: Fakhar Zaman
                Country: Pakistan
                Age: 29
                Specification: Left Handed BAtsman ''' )
                elif player == 11:
                    print('''
                Name: David Wiese
                Country: South Africa
                Age: 35
                Specification: Bowling All-Rounder''' )
            elif choice == 4:
                print('''
            ** Squad **
            1. Mohammad Rizwan (C)(WK)
            2. Shan Masood (VC)
            3. Shahid Afridi
            4. Usman Qadir 
            5. Imran Tahir 
            6. James Vince
            7. Sohaib Maqsood
            8. Sohail Khan
            9. Sohail Tanveer
            10.Shahnawaz Dhani
            11.Rilee Roussow ''')
                player = int(input("Enter player number: "))
                if player == 1:
                    print('''
                __________
                ** Players **
                Name: Mohammad Rizwan
                Country: Pakistan
                Age: 28
                Specification: WicketKeeper Batsman
                Batsman: Right-Handed Batsman
                __________''' )
                elif player == 2:
                    print('''
                __________
                ** Players **
                Name: Shan Masood
                Country: Pakistan
                Age: 25
                Specification: Left Handed Batsman
                __________''' )
                elif player == 3:
                    print('''
                __________
                Name: Shahid Afridi
                Country: Pakistan
                Age: 40
                Specification: Batting All-Rounder
                Batting style: Right-Handed Batsman
                Bowling Style: Right Arm Offspin
                __________''' )
                elif player == 4:
                    print('''
                Name: Usman Qadir
                Country: Pakistan
                Age: 24
                Specification: Spin Bowlwer
                __________''' )
                elif player == 5:
                    print('''
                Name: Imran Tahir
                Country: South Africa
                Age: 37
                Specification: Spin Bowler''' )
                elif player == 6:
                    print('''
                Name: James Vince
                Country: England
                Age: 33
                Specification: Batsman''' )
                elif player == 7:
                    print('''
                Name: Sohaib Maqsood
                Country: Pakistan
                Age: 27
                Specification: Batsman''' )
                elif player == 8:
                    print('''
                Name: Sohail Khan
                Country: Pakistan
                Age: 36
                Specification: FAst Bowler''' )
                elif player == 9:
                    print('''
                Name: Sohail Tanveer
                Country: Pakistan
                Age: 34
                Specification: Fast Bowler''' )
                elif player == 10:
                    print('''
                Name: Shahnawaz Dhani
                Country: Pakistan
                Age: 22
                Specification: Fast Bowler''' )
                elif player == 11:
                    print('''
                Name: Rilee Roussow
                Country: South Africa
                Age: 35
                Specification: Left HAnded Batsaman''' )
            elif choice == 5:
                print('''
            ** Squad **
            1. Wahab Riaz (C)
            2. Shoaib Malik (VC)
            3. Kamran AKmal (Wk)
            4. Imam Ul Haq 
            5. M Irfan 
            6. David Miller
            7. Saqib Mehmood
            8. M Imran
            9. Kohler Cadmore
            10.Ammad Butt
            11.Haider Ali ''')
                player = int(input("Enter player number: "))
                if player == 1:
                    print('''
                __________
                ** Players **
                Name: Wahab Riaz
                Country: Pakistan
                Age: 34
                Specification: Bowling All_Rounder
                Batsman: Right-Handed Batsman
                __________''' )
                elif player == 2:
                    print('''
                __________
                ** Players **
                Name: Shoaib Malik
                Country: Pakistan
                Age: 41
                Specification: Right Handed Batsman
                __________''' )
                elif player == 3:
                    print('''
                __________
                Name: Kamran Akmal
                Country: Pakistan
                Age: 37
                Specification: WicketKeeper BAtsman
                Batting style: Right-Handed Batsman
                __________''' )
                elif player == 4:
                    print('''
                Name: Imam Ul Haq
                Country: Pakistan
                Age: 27
                Specification: Left Handed Batsman
                __________''' )
                elif player == 5:
                    print('''
                Name: M Irfan
                Country: Pakistan
                Age: 36
                Specification: Fast Bowler''' )
                elif player == 6:
                    print('''
                Name: David Miller
                Country: South Africa
                Age: 32
                Specification: Left Handed Batsman''' )
                elif player == 7:
                    print('''
                Name: Saqib Mehmood
                Country: England
                Age: 35
                Specification: FAst Bowler''' )
                elif player == 8:
                    print('''
                Name: M Imran
                Country: Pakistan
                Age: 22
                Specification: FAst Bowler''' )
                elif player == 9:
                    print('''
                Name: Kohler Cadmore
                Country: Australia
                Age: 23
                Specification: Right Handed Batsman''' )
                elif player == 10:
                    print('''
                Name: Ammad Butt
                Country: Pakistan
                Age: 26
                Specification: Fast Bowling All-Rounder''' )
                elif player == 11:
                    print('''
                Name: Haider Ali
                Country: Pakistan
                Age: 22
                Specification: Right HAnded Batsaman''' )
            elif choice == 6:
                print('''
            ** Squad **
            1. Sarfraz Ahmed (C)(WK)
            2. M NAwaz (VC)
            3. Azam Khan
            4. Chris GAyle
            5. Ben Cutting 
            6. Andre Russel
            7. Zahid Mehmood
            8. M HAsnain
            9. Naseem Shah
            10.Azam Khan
            11.Dale Steyn ''')
                player = int(input("Enter player number: "))
                if player == 1:
                    print('''
                __________
                ** Players **
                Name: Sarfraz Ahmed
                Country: Pakistan
                Age: 32
                Specification: WicketKeeper Batsman
                Batsman: Right-Handed Batsman
                __________''' )
                elif player == 2:
                    print('''
                __________
                ** Players **
                Name: M Nawaz
                Country: Pakistan
                Age: 30
                Specification: Left Arm Spin Bowler
                __________''' )
                elif player == 3:
                    print('''
                __________
                Name: Azam Khan
                Country: Pakistan
                Age: 24
                Specification: Batsman
                Batting style: Right-Handed Batsman
                __________''' )
                elif player == 4:
                    print('''
                Name: Christopher Henry GAyle
                Country: West Indies
                Age: 42
                Specification: Batsman 
                Batting Style: Left HAnded Batsman
                Bowling Style: Left Arm Spin
                __________''' )
                elif player == 5:
                    print('''
                Name: Ben Cutting
                Country: Australia
                Age: 34
                Specification: Fast Bowling All-Rounder''' )
                elif player == 6:
                    print('''
                Name: Andre Russel
                Country: West Indies
                Age: 33
                Specification: Bowling All-Rounder''' )
                elif player == 7:
                    print('''
                Name: Zahid Mehmood
                Country: Pakistan
                Age: 24
                Specification: Spin Bowler''' )
                elif player == 8:
                    print('''
                Name: M HAsnain
                Country: Pakistan
                Age: 20
                Specification: FAst Bowler''' )
                elif player == 9:
                    print('''
                Name: Naseem Shah
                Country: Pakistan
                Age: 20
                Specification: Fast Bowler''' )
                elif player == 10:
                    print('''
                Name: Azam Khan
                Country: Pakistan
                Age: 24
                Specification: Batsman''' )
                elif player == 11:
                    print('''
                Name: Dale Steyn
                Country: South Africa
                Age: 36
                Specification: Fast Bowler''' )

        elif action == 2:
            print('''
            __________
            ** Teams **
            1. Islamabad United
            2. Karachi Kings
            3. Lahore Qalandars
            4. Multan Sultan
            5. Peshawar Zalmi
            6. Quetta Gladiators
            7. Exit
            __________''')
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print('''
                ---------------------------------------
                Islamabad is the most fortunate side of
                the PSL who stood on the winning floor
                twice. It Represents the Capital city of
                Pakistan. This squad played the centalizing
                cricket brand in HBL PSL. They stood on the
                winning floor in PSL 2016 and 2018. 
                ---------------------------------------''')
            elif choice == 2:
                print('''
                ---------------------------------------------
                Karachi Kings is the defending Champion of PSL
                2020. It is one of the aggressive and brilliant
                side for Pakistan Cricket that personifies one 
                of the biggest city of PAkistan 'Karachi'. The 
                frenchise is known for Epic cricket in PSL. 
                ----------------------------------------------''')
            elif choice == 3:
                print('''
                ---------------------------------------------
                Qalandars is admitted as one of the fantastic  
                and brilliant t20 squad in PSL. This lineup is
                also famous for its passion and played exciting
                and thrilling matches oer the last five years.
                They are the runner-up in PSL 5.  
                ----------------------------------------------''')
            elif choice == 4:
                print('''
                ------------------------------------------------
                Multan Sultans is a brilliant domestic t20 side   
                in Pakistan Super League. It was on the top of 
                the points table after the first round of HBL 
                Pakistan Super League. They play gorgeous cricket
                and has a great combination of seniors and juniors
                overseas and local cricketers. 
                ------------------------------------------------''')
            elif choice == 5:
                print('''
                ---------------------------------------------
                Peshawar Zalmi is one of the epic team of the
                domestic cricket that peronifies the city of 
                Peshawar. A PAkistani Business tycon JAved Khan
                Afridi is the properiter of the frenchise. Zalmi
                stood on the winning floor in PSL 2017 under the
                captaincy of a Legendry Cricketer Daren Sammy. 
                Wahab Riaz is the current Skipper of the team.
                ----------------------------------------------''')
            elif choice == 6:
                print('''
                -----------------------------------------------
                Quetta Gladiators is consider as one of the most
                successful team of HBL PSL. They Played awesomwe 
                cricket throughout the league. Gladiators were 
                the runnerup of 2016 and 2017 HBL PSL. They stood
                on the winning floor in PSL 2019. Gladiators is 
                lead by one of the successful captain of Pakistan.
                -----------------------------------------------''')
            else:
                print("Choose a right number! ")
        elif action == 3:
            print('''
            ----------------------------
            ** Team Staff **
            1. Islamabad United
            2. Karachi Kings
            3. Lahore Qalandars
            4. Multan Sultan
            5. Peshawar Zalmi
            6. Quetta Gladiators
            7. Exit
            ----------------------------''')
            coaches = int(input("Enter your Choice: "))
            if coaches == 1:
                print('''
                ------------------------------------------
                Team: Islamabad United
                Head Coach: Johan Botha
                Assitant Coach: Saeed Ajmal
                Fielding and Fitness Trainer: Corey Rutgers
                Owner: Ali Naqvi
                Home GRound: RAwalpindi Cricket Stadium
                ------------------------------------------''')
            elif coaches == 2:
                print('''
                ------------------------------------
                Team: Karachi Kings
                Head Coach: Harschelle Gibbs
                Bowling Coach: Waseem Akram 
                Batting Coach: Faisal Iqbal
                Owner: Salman Iqbal
                Home GRound: National Stadium Karachi
                ------------------------------------'''  )
            elif coaches == 3:
                print('''
                -----------------------------------
                Team: Lahore Qalandars
                Head Coach: Aaqib Javed
                Batting Coach: Mansoor Rana 
                Fitness Trainer: Shehzad Butt
                Owner: Sameen Rana
                Home GRound: Gaddafi Stadium Lahore
                -----------------------------------'''  )
            elif coaches == 4:
                print('''
                -----------------------------------
                Team: Multan Sultans
                Head Coach: Andy Flowers
                Bowling Coach: Azhar Mehmood
                spin Bowling Coach: Mushtaq Ahmed
                Owner: Ali Khan Tareen
                Home GRound: Multan Cricket Stadium
                -----------------------------------'''  )
            elif coaches == 5:
                print('''Peshawar Zalmi
                -------------------------------
                Head Coach: Daren Sammy
                Batting Coach: HAshim Amla
                Owner: Javed Khan Afridi
                Home GRound: Arbab Niaz Stadium
                -------------------------------'''  )
            elif coaches == 6:
                print('''
                ----------------------------------
                Team: Quetta Gladiators
                Head Coach: Moin Khan
                BAtting Coach: Sir Vivian Richard
                Bowling Coach: Umar Gul
                Owner: Nadeem Umar
                Home GRound: Buggti Cricket Stadium
                ----------------------------------'''  )
            
        elif action == 4:
            print('''
            ** Ticket Reservation System **
            1. Reserve Tickets
            2. Return Tickets
            3. Check Status
            4. Exit
            __________''')
            ch = int(input("Enter your choice: "))
            if ch == 1:
                list = [2,3,4,5,8,12,15,16,18,20,22.25,27]
                people = int(input("\nHow many tickets you want: "))
                name_l = []
                age_l = []
                gender_l = []
                country_l = []
                seat_l = []
                listreturn = []
                for p in range(people):
                    print("__________")
                    print("Available seats are: ",list)
                    seat = int(input("Enter the seat number: "))
                    if seat in list:  
                        name = str(input("Name : "))
                        name_l.append(name)
                        age  = int(input("Age  : "))
                        age_l.append(age)
                        gender  = str(input("Gender : "))
                        gender_l.append(gender)
                        country  = str(input("Country : "))
                        country_l.append(country)
                        seat_l.append(seat) 
                        list.remove(seat)
                        print("Available seats are: ", list)
                    listreturn = list
                def profile():
                    listreturn = []
                    try:
                        x = 0
                        print("__________")
                        print("\n\nTotal Ticket : ",people)
                        for p in range(1,people+1):
                            print("__________\n")
                            print("\tTicket : ",p)
                            print("\tSeat Number : ", seat_l[x])
                            print("\tName : ", name_l[x])
                            print("\tAge  : ", age_l[x])
                            print("\tGender : ",gender_l[x])
                            print("\tCountry : ",country_l[x])
                            x += 1
                            print("__________")
                        listreturn = list
                    except:
                        print("------------------------------------------------")
                        print("number seat is not present, Try another!")
                        print("------------------------------------------------")
                profile()
            elif ch == 2:
                    print("----------------------")
                    print("Available Seats are: ",listreturn)
                    numberticket = int(input("How many tickets you want to return: "))
                    list = [2,3,4,5,8,12,15,16,18,20,22.25,27]
                    if numberticket<=people:
                        i=1
                        while i <= numberticket:
                            returnticket = int(input("Enter the number of seat you want to return: "))
                            if returnticket in list:
                                listreturn.append(returnticket)
                                print(listreturn)
                                i += 1
                            else:
                                print("You didn't booked", returnticket, "seat number ticket")
                    else:
                        print("You have booked",people)   
            elif ch == 3:
                try:
                    print("-------------------------\n")
                    print("Hi", username, "Your Details are as follows: ")
                    profile()
                except:
                    print("You have not Reserve any ticket. ")
    
        else:
            exit()
    print('''Thanks for your login! 
            __________''')
 else:
     print("You entered your Email wrong. Enter correct Email ")
else:
    print("You entered your Email wrong. Enter correct Email ")