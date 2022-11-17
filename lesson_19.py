st = "Замените в этой строке все появления буквы 'о' на букву 'О', кроме первого и последнего вхождения."
first = st.find("о")
second = st.rfind("о")
st_new = st[first+1:second]
st_new = st_new.replace("о", "О")
print(st[:first+1] + st_new + st[second:])