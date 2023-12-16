import qrcode as QR
#  Use Make Function and Put The Url You can add Text also 
img = QR.make("https://www.intel.com/content/www/us/en/developer/tools/oneapi/optimization-for-tensorflow.html?cid=sem&source=sa360&campid=2023_q4_iags_in_iagsoapie_iagsoapiee_awa_text-link_exact_cd_dpd-oneapi-tensor-flow_3500139201_google_div_oos_non-pbm_intel&ad_group=machine_learning_performance_exact&intel_term=tensorflow+tutorial&sa360id=43700078272510939&gad_source=1&gclid=Cj0KCQiAsvWrBhC0ARIsAO4E6f9R-LjQo6PnOZayEATMzHyNo1-SN3Nv0M9nAE_lznTQgtFfkw3yF-AaAgVyEALw_wcB&gclsrc=aw.ds")
img.save("TensorFlow Details.png")

