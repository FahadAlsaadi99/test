import pandas as pd
import numpy as np
import streamlit as st
#import arabic_reshaper as ar 
#df = pd.read_excel(r"C:\Users\foooo\Downloads\Riyadh_Aqqar.xlsx", sheet_name=0)

#
st.markdown("""
    <style>
    .custom-title {
        font-size: 70px;
        color: blue;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="custom-title">هل فيه شقق رخيصة بالرياض؟</p>', unsafe_allow_html=True)
#st.image(r"C:\Users\foooo\OneDrive\سطح المكتب\photo pro\Screenshot 2024-08-10 170406.png", use_column_width=True)


re_ = ar.reshape('أكيد أنت الحين تسأل نفسك: "كيف ألقى شقة سعرها معقول وبمميزات تناسب احتياجاتي، في حي كويس وياليت لو كان قريب من شغلي الجديد؟"للأعزاء اللي ناوين ينقلون للرياض لبداية جديدة، بسهل عليكم الأمور وأعرض لكم أسعار الشقق في الرياض من زوايا مختلفة. بساعدك تحصل اللي يناسبك 🙂.')

st.header(re_)
st.write("") 
st.write("")
st.write("") 
st.write("")
st.write("")

st.header(r'بالبداية أول ما يخطر على بال الشخص اللي راح يسكن في مكان جديد هو الحي وأسعار الشقق فيه, هنا بعرض لك الأسعار المتفاوتة لمعظم أحياء الرياض أو خلينا نقول أشهر الأحياء القريبة من أماكن العمل.')
#st.map(df)
#st.image(r"C:\Users\foooo\OneDrive\سطح المكتب\photo pro\Screenshot 2024-08-10 170406.png", use_column_width=True)
st.write("تشارت يستعرض أسعار الشقق في الأحياء المعروفة أو القريبة لمقرات العمل المختلفة") 
st.write("")
st.write("") 
st.write("")
aa = 'يمكن تسأل الحين: "وش هي الأحياء الأغلى والأرخص؟" البيانات تقول إن حي الملقا من أغلى الأحياء في أسعار الشقق. ممكن تسأل نفسك ليه، وأنا نفسي محتار مثلك. أما حي المناخ، فهو من الأحياء الأرخص. يمكن أول مرة تسمع عنه، لكن لا تشيل هم، بعطيك أرخص 5 أحياء وأغلى 5 أحياء عشان تقارن بينهم وتختار اللي ودك فيه.'
st.header(aa)

st.write("(تشارت يعرض أغلى وأرخص 5 أحياء)") 
st.write("")
st.write("") 
#st.write("(تشارت يعرض أغلى وأرخص 5 أحياء)")
st.write("")
st.write("") 
st.header("لسا باقي مو متأكد من اختيارك؟ ممكن تفكر بالعوامل اللي تأثر على سعر الشقة؟ هنا بوضح لك إيش العوامل اللي ممكن تأثر على سعر الشقة, هل الدور الأول يفرق عن الثاني, هل عدد الغرف تفرق؟ وأكثر!")

st.write("(تشارت يوضح الفاكتورز المؤثرة على سعر الشقق)")


st.header('طيب عزيزي القارئ هل ودك تريح نفسك وتشتري شقة مؤثثة؟ لكن ودك تعرف أسعارها وفرقها عن الغير مؤثثة؟ البيانات هنا توضح لك أن…..')

st.write("(تشارت يقارن بين أسعار الشقق المؤثثة والغير مؤثثة)")

st.header('بالنهاية أتمنى أنك استفدت وهوّنت عليك ضغط النقل لعاصمة المستقبل الحبيبة الرياض.')







