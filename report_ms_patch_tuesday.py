import functions_report_ms_patch_tuesday

year = "2021"
months = list()
# months.append("January")
months.append("February")

rewrite_flag = True
# rewrite_flag = False

for month in months:
    functions_report_ms_patch_tuesday.make_ms_patch_tuesday_report(year=year,
                                                                   month=month,
                                                                   rewrite_flag=rewrite_flag)
