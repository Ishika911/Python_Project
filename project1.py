import qrcode
#Taking UPI ID as a input
upi_id = input("enter your UPI ID =")
#defining the payment URL based on the UPI ID and the payment app
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipent%20Name&mc =1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipent%20Name&mc =1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipent%20Name&mc =1234'
#Create QR codes for each payment app
phonepe_url=qrcode.make(phonepe_url)
paytm_url=qrcode.make(paytm_url)
google_pay_url=qrcode.make(google_pay_url)
#save to QR code to image file
phonepe_url.save(r'c:\Users\DELL\Downloads\phonepeimages.png')
paytm_url.save(r'c:\Users\DELL\Downloads\paytm.png')
google_pay_url.save(r'C:\Users\DELL\Downloads\googlepayimages.png')
#Display the QR Codes
phonepe_url.show()
paytm_url.show()
google_pay_url.show()




