import qrcode as QR
from PIL import Image
The_Qr = QR.QRCode(version=1,error_correction = QR.constants.ERROR_CORRECT_H, box_size = 10, border=4)
The_Qr.add_data("https://www.intel.com/content/www/us/en/developer/tools/oneapi/optimization-for-tensorflow.html?cid=sem&source=sa360&campid=2023_q4_iags_in_iagsoapie_iagsoapiee_awa_text-link_exact_cd_dpd-oneapi-tensor-flow_3500139201_google_div_oos_non-pbm_intel&ad_group=machine_learning_performance_exact&intel_term=tensorflow+tutorial&sa360id=43700078272510939&gad_source=1&gclid=Cj0KCQiAsvWrBhC0ARIsAO4E6f9R-LjQo6PnOZayEATMzHyNo1-SN3Nv0M9nAE_lznTQgtFfkw3yF-AaAgVyEALw_wcB&gclsrc=aw.ds")
The_Qr.make(fit=True)
img = The_Qr.make_image(fill_color = "red",back_color = "black")
img.save("Tensorflow_web.png")