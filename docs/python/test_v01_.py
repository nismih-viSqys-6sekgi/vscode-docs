import openpyxl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import re
import math
import datetime
from matplotlib.ticker import FormatStrFormatter



# 品名
name_cell = ''

# ベキ動率 %
power_rate = 100

# サイクルタイム s
cas_cycle = 78.0

# 指示数 個
cas_shot = 247

# PL入数 [個]
pl_qua = 80

# 前勤端数 [+個]
f_frc = 0

# 味見品 PL (No.)
insert_pl = 0
# 味見品 [個]
insert_n = 0

# 生産済み PL (No.)
comp_pl = 0

# 稼働時間 分
time_dic = {
	'8時台 ': 50
	,'9時台 ': 60
	,'10時台': 60
	,'11時台': 60
	,'12時台': 10
	,'13時台': 60
	,'14時台': 60
	,'15時台': 60
	,'16時台': 30
	}





time_now = datetime.datetime.now()
print(f'{time_now.hour}:{time_now.minute}')

p_r = power_rate / 100

name_str = re.findall('[,]+',
name_cell)

name_n = len(name_str)
print('取数')
print(name_n + 1)
print()

n_time_list = []
time_h_v_list = []
n_pl = []
number_n = []
rest_pl = []

# PL毎の時間
def calc_rest_time(cas_cycle, cas_shot, pl_qua, f_frc):
	
	# 時間計画数 ヶ/h
	time_n = int(3600 / cas_cycle * p_r)
	
	# [入数] * PL
	rest_n = int((cas_shot - f_frc - insert_n) / pl_qua)
	
	# [端数+]
	b_frc = (cas_shot - f_frc -insert_n) - pl_qua * rest_n
	rest_pl.append(f_frc)
	
	for i in range(rest_n):
		rest_pl.append(pl_qua)
		
	total_time = []
	rest_pl.append(b_frc)
	
	if insert_pl > 0:
		rest_pl.insert(insert_pl, insert_n)
			

	
	
	
	total_n = sum(rest_pl)
	to_ti = total_n / time_n
	total_time.append(to_ti)
	tt = 0
	for i in rest_pl:
		tt += i
		total_time.append((total_n - tt) / time_n)
		rest_time = []
		for total_time_v in total_time:
			
			if name_n > 0:
				h = total_time_v / (name_n + 1)
				total_time_v = h
				f, i = math.modf(total_time_v)
				print(f , i)
				f_m = int(round(f, 2) * 60)
				i_h = int(i)
				t_time = datetime.time(hour = i_h, minute = f_m)
				print(t_time)
				
				if f_m <= 9:
					time_v = f' {i_h} H 0{f_m} M'
					rest_time.append(time_v)
					
				else:
					time_v = f' {i_h} H {f_m} M'
					rest_time.append(time_v)
					
			else:
				f, i = math.modf(total_time_v)
				f_m = int(round(f, 2) * 60)
				i_h = int(i)
				t_time = datetime.time(hour = i_h, minute = f_m)
						
				if f_m <= 9:
					time_v = f' {i_h} H 0{f_m} M'
					rest_time.append(time_v)

				else:
					time_v = f' {i_h} H {f_m} M'
					rest_time.append(time_v)
	
	for e, (i, t) in enumerate(zip(rest_pl, rest_time)):
		
		if i == 0:
			continue
			
		if e == 0:
			e = '前'
			print(f'No.{e} [+{i}] 個/PL {t}')
		elif i < pl_qua:
			print(f'No.{e} [{i}+] 個/PL {t}')
		else:
			print(f'No.{e} [{i}] 個/PL {t}')
				
		

	rest_pl_t = 0
	for i in rest_pl[comp_pl + 1:]:
		rest_pl_t += i
		t_rest = rest_pl_t / time_n
		m, h = math.modf(t_rest)
		
		m_m = int(round(m, 2) * 60)
		h_h = int(h)
		
		rest_t = datetime.time(hour = h_h, minute = m_m)
		
		if m_m <= 9:
			time_h_m = f' {h_h} H 0{m_m} M'
			
		else:
			time_h_m = f' {h_h} H {m_m} M'
	
			
	now_time = datetime.timedelta(hours = time_now.hour, minutes = time_now.minute)
	
	basetime = datetime.timedelta(hours = h_h, minutes = m_m)
	
	Scheduled_time = now_time + basetime
	print()
	print('残り数')
	print(rest_pl_t)
	print(time_h_m)
	print(now_time)
	print(basetime)
	print(Scheduled_time)
	print()
	
	
							
calc_rest_time(cas_cycle,cas_shot, pl_qua, f_frc)






# 時間毎の数
def cal_time(cas_cycle, cas_shot, time_dic):
	cal_ti = cas_cycle * cas_shot
	print(cal_ti)
	h_time = int(3600 / cas_cycle * p_r)
	print(f'{h_time}  時間ショット数')
	print(f'ベキ動率  {power_rate} %')
	print()
	n_time_v = 0
	
	for k, v in time_dic.items():
		t = v / 60 
		time_h_v = int(t * h_time)
		n_time_v += time_h_v
		n_time_list.append(n_time_v)
		time_h_v_list.append(time_h_v)
		print(f'{k} {time_h_v} 個   合計 {n_time_v}')
		
	print()
	
	cas_time = cas_shot / h_time

	if name_n > 0:
		cas_time = cas_shot / h_time /  (name_n + 1)
		f, i = math.modf(cas_time)
		print(f , i)
		f_m = int(round(f, 2) * 60)
		print(f_m)
		i_h = int(i)
		print(i_h)
		t_time = datetime.time(hour = i_h, minute = f_m)
		print(t_time)
		
		if f_m <= 9:
			print()
			print(f'指示数 {cas_shot} 個')
			time_v = f'良品取時間  {i_h} H 0{f_m} M'
			print(time_v)
			
		else:
			print()
			print(f'指示数 {cas_shot} 個')
			time_v = f'良品取時間  {i_h} H {f_m} M'
			print(time_v)
		
	
	else:
		f, i = math.modf(cas_time)
		print(f , i)
		f_m = int(round(f, 2) * 60)
		print(f_m)
		i_h = int(i)
		print(i_h)
		t_time = datetime.time(hour = i_h, minute = f_m)
		print(t_time)
			
		if f_m <= 9:
			print()
			print(f'指示数 {cas_shot} 個')
			time_v = f'良品取時間  {i_h} H 0{f_m} M'
			print(time_v)
			
		else:
			print()
			print(f'指示数 {cas_shot} 個')
			time_v = f'良品取時間  {i_h} H {f_m} M'
			print(time_v)



cal_time(cas_cycle, cas_shot, time_dic)




 
# ラベル
labels = time_dic.keys()
# 値
values = n_time_list

# データ操作用
df = pd.DataFrame({"label": labels, "value": values}, columns=["label", "value"])
# 「値」の降順にデータを並び替える
# df = df.sort_values(by="value", ascending=False)
# 累積和を求める
df["accum"] = np.cumsum(df["value"])
# 比率の累計を求める
df["accum_percent"] = df["accum"] / sum(df["value"]) * 100
 
# サイズ指定
fig = plt.figure(dpi=100, figsize=(7.80, 5.44))
# 軸関係の表示
ax = fig.add_subplot(111)
 
# データ数のカウント
data_num = len(df)
 
# 棒グラフの描画
ax.bar(range(data_num), df["value"], width=0.4, color="#3366ff", edgecolor="#0f1e4b", label="個数")
ax.set_xticks(range(data_num))
ax.set_xticklabels(df["label"].tolist())
ax.set_xlabel("(時刻)")
ax.set_ylabel("(個数)")
ax.set_yticks(np.arange(0, cas_shot + 20, 50))
ax.set_ylim([0, cas_shot + 50])
'''
# 折れ線グラフの描画
ax_add = ax.twinx()
ax_add.plot(range(data_num), df["accum_percent"], color="#ff8181", linewidth=2.5,
marker="o",markersize=8, markeredgecolor="#000081", markeredgewidth= 0.7,
            label="比率の累計")
ax_add.set_ylim([0, 120])
ax_add.set_ylabel("(比率の累計)")

# 軸目盛りのフォーマット
ax_add.yaxis.set_major_formatter(FormatStrFormatter("%.1f"))
'''
 
l1 = ax.axhline(y= cas_shot, xmin=0.05, xmax=0.95,color='red', lw=2, ls='--', alpha=0.6)

l1.set_label('指示数')



plt.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0, fontsize=18)


 
''' 
# 凡例
# それぞれの軸でデータとラベルを抽出
ax_handler, ax_label = ax.get_legend_handles_labels()
ax_add_handler, ax_add_label = ax_add.get_legend_handles_labels()
# 凡例をまとめて出力
ax.legend(ax_handler + ax_add_handler, ax_label + ax_add_label, bbox_to_anchor=(1.15, 0.55), loc='upper left')
'''
# 余白調整
plt.subplots_adjust(left=0.08, right=0.73, bottom=0.1, top=0.96)
 
# グラフを画像保存
#plt.savefig("result.xlsx", facecolor="white")


plt.show()

print()
print()
print()

