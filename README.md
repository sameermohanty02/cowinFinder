# cowinFinder
Cowin Finder is a tool to automatically search for vaccine slots as per Pin  code or District name for next 7 days.
This tool will work irrespective of the Operating system.
## Prerequisite:
Installation of python.

Steps to install python\
https://www.youtube.com/watch?v=UvcQlPZ8ecA - For windows
https://www.youtube.com/watch?v=Br2xt6B57SA - For Linux
##Installation of Cowin Finder:
clone the git repo:
```text
git clone https://github.com/sameermohanty02/cowinFinder.git
```

go to directory cowinFinder
```text
cd cowinFinder
```
Install the tool:
```text
pip install --editable .

or

python3 -m pip install -editable .
```

##Run the Tool:
Enter the below Command:

```text
cowin find
```

```text
Hello, Welcome to Cowin Vaccine finder tool!

Select Options:

[1] Find Vaccine with District
[2] Find vaccine with Pincode
[3] Find your Beneficiaries
[q] Quit

> Enter the option: 1

 Find Vaccine slots by Districts

 Find Vaccine slots by Districts
>> Please enter the age: 22
>> Please enter the District Name: Khurda
>> Starting search for Covid vaccine slots!
=========================
Name : Capital Hospital BBSR1
Available Capacity : 83
Date : 17-05-2021
Address : Unit 6 Capital Hospital BBSR
Pincode : 751001
=========================

```
Find beneficiary:
```text
> Enter the option: 3
Enter your Mobile number: XXXX
Enter the otp you received: XXXX
<PreparedRequest [GET]>
=========================
Name: Sameer Mohanty
Beneficiary reference id: XXXXX
Beneficiary vaccination status: XXX
Beneficiary photo ID type: XXXX
Beneficiary appointment details: XXXXX
Beneficiary photo ID: XXXXX
=========================

```

DISCLAIMER\
Important:\
This is a proof of concept project. I do NOT endorse or condone, in any shape or form, automating any monitoring/booking tasks. Developed for Educational Purpose; Use at your own risk. I SHOULD NOT BE DEEMED RESPONSIBLE FOR ANY LEGAL CONCERNS.
This CANNOT book slots automatically. It doesn't skip any of the steps that a normal user would have to take on the official portal. You will still have to enter the OTP. This just helps to do it from Console rather than through Official WebApps/Apps.