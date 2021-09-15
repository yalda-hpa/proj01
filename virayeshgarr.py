matn = input('متن خود را جهت ویرایش وارد کنید!')
nadorost = input('کلمه ای که در متنتان نیاز ب ویرایش دارد را وارد کنید!')
dorost = input('کلمه ای که جهت جا به جایی با حرف نادرست مد نظر دارید را وارد کنید!')
charkhesh = 0
tedad_matn = len(matn)
tedad_nadorost = len(nadorost)
while charkhesh < tedad_matn:
	if nadorost == matn[charkhesh : charkhesh + tedad_nadorost]:
		tedad_matn = len(matn)
		matn = matn[:charkhesh] + dorost + matn[charkhesh + tedad_nadorost:]
	charkhesh = charkhesh + 1
print(matn)