import wx
import csv
import numpy as np
import sys
import os








class BioMCFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,title="ZhangTao's CSV",style=wx.DEFAULT_FRAME_STYLE)
		self.SetPosition((400,300))
		self.Bind(wx.EVT_CLOSE,self.wx_exit_funcs)
		self.create_menu()
		self.statusbar=self.CreateStatusBar()
		self.create_plot_panel()
		reload(sys)
		sys.setdefaultencoding('gb18030')
		self.kg=0
		wx.MessageBox(u'您好，您可以通过按钮或者工具菜单或者快捷键'+'\n'+u'来合并a.csv和b.csv文件',"ZhangTao's CSV",wx.OK|wx.ICON_INFORMATION)
		
	def wx_exit_funcs(self,event):
		self.statusbar.SetStatusText("We're Exiting,Please Wait......")
		self.Destroy()
	def on_about(self,event):
		msg0="""
	* CopyRight 2015 Zhang Tao All Rights Reserved
	
	* EDITION:CSV_Operating
	
	* SN:+86-13552783774
	
	* Version:1.0
	
	* It Is Tool Which Makes Your Idea Become Reality
		"""
		show_about_help=wx.MessageDialog(self,msg0,"ZhangTao's CSV",wx.OK)
		show_about_help.ShowModal()
		show_about_help.Destroy()		
	def hebing_c_funcs(self,event):
		self.hebing_c.Enable(0)
		self.hebing.Enable(0)
		self.yuwenjiang.Enable(1)
		self.yuwen_j.Enable(1)
		self.yuwensheng.Enable(1)
		self.yuwen_s.Enable(1)
		
		self.shuxuejiang.Enable(1)
		self.shuxue_j.Enable(1)
		self.shuxuesheng.Enable(1)
		self.shuxue_s.Enable(1)		
		
		self.xuehaojiang.Enable(1)
		self.xuehao_j.Enable(1)
		self.xuehaosheng.Enable(1)
		self.xuehao_s.Enable(1)		
		
		
		
		
		
		str_rows_arraya=open('a.csv').readlines()
		str_rows_arrayb=open('b.csv').readlines()
		for j in xrange(0,len(str_rows_arraya)):
			every_row_arraya=str_rows_arraya[j].rstrip().split(',')
			if 5<=j<=19999:
				every_row_arrayb=str_rows_arrayb[j-5].rstrip().split(',')
				every_row_arraya=every_row_arraya[:]+[every_row_arrayb[1]]
			str_rows_arraya[j]=','.join(every_row_arraya)+'\n'
		open('c.csv','wb').write('NO'+','+'YUWEN'+','+'SHUXUE'+'\n'+''.join(str_rows_arraya))		
		
		
		
	def paixu_funcs(self,event,cs0):
		
		if cs0[0]==0:
			self.yuwenjiang.Enable(0)
			self.yuwen_j.Enable(0)
		elif cs0[0]==1:
			self.yuwensheng.Enable(0)
			self.yuwen_s.Enable(0)
			
		elif cs0[0]==2:
			self.shuxuejiang.Enable(0)
			self.shuxue_j.Enable(0)			
		elif cs0[0]==3:
			self.shuxuesheng.Enable(0)
			self.shuxue_s.Enable(0)
			
		elif cs0[0]==4:
			self.xuehaojiang.Enable(0)
			self.xuehao_j.Enable(0)			
		elif cs0[0]==5:
			self.xuehaosheng.Enable(0)
			self.xuehao_s.Enable(0)
			
			
			
		if self.kg==0:
			self.file=open('c.csv','rb')
			self.str_rows_arrayc=csv.DictReader(self.file)
			self.aar=np.array([])
			for i in self.str_rows_arrayc:
				self.kg+=1
				if self.kg<=5 or self.kg>20000:
					self.aar=np.concatenate((self.aar,np.array([{'SHUXUE': 0, 'YUWEN': int(i['YUWEN']), 'NO': int(i['NO'])}])))
				elif 5<self.kg<=20000:
					self.aar=np.concatenate((self.aar,np.array([{'SHUXUE': int(i['SHUXUE']), 'YUWEN': int(i['YUWEN']), 'NO': int(i['NO'])}])))
		li = sorted(self.aar, key=lambda s: s[cs0[1]],reverse=cs0[2])
		file=open(cs0[3],'w')
		file.write('NO'+','+'YUWEN'+','+'SHUXUE'+'\n')
		for x in li:
			file.write('%d,%d,%d\n'%(x['NO'],x['YUWEN'],x['SHUXUE']))
		file.close()
		
	def view_files_funcs(self,event):
		
		open_file=wx.FileDialog(self,message=u"浏览或打开文件",defaultDir=os.getcwd(),defaultFile="*.csv",wildcard="CSV (*.csv)|*.csv",style=wx.OPEN)

		if open_file.ShowModal()==wx.ID_OK:
			data_file_path=open_file.GetPath()
			os.popen(data_file_path)
		open_file.Destroy()
		
		
		
		
		
		

	def create_menu(self):

		self.wx_menu_bar=wx.MenuBar()
		self.file_menu=wx.Menu()
		
		self.view_files=self.file_menu.Append(-1,u"浏览文件\tCtrl-A", u"浏览a.csv等文件")
		self.Bind(wx.EVT_MENU,self.view_files_funcs,self.view_files)
		self.file_menu.AppendSeparator()	
		
		
		
		
		self.hebing=self.file_menu.Append(-1,u"合并为c.csv\tCtrl-B", u"将a.csv和b.csv合并为c.csv")
		self.Bind(wx.EVT_MENU,self.hebing_c_funcs,self.hebing)
		self.file_menu.AppendSeparator()
		
		
		self.yuwenjiang=self.file_menu.Append(-1,u"语文降序\tCtrl-C", u"按语文成绩降序排列生成:语文降序排列.csv")
		self.Bind(wx.EVT_MENU,lambda evt, cs0=[0,'YUWEN',1,u'语文降序排列.csv'] :self.paixu_funcs(evt,cs0),self.yuwenjiang)
		self.yuwenjiang.Enable(0)
		self.file_menu.AppendSeparator()
		
		
		self.yuwensheng=self.file_menu.Append(-1,u"语文升序\tCtrl-D", u"按语文成绩升序排列生成:语文升序排列.csv")
		self.Bind(wx.EVT_MENU,lambda evt, cs0=[1,'YUWEN',0,u'语文升序排列.csv'] :self.paixu_funcs(evt,cs0),self.yuwensheng)
		self.yuwensheng.Enable(0)
		self.file_menu.AppendSeparator()
		
		
		self.shuxuejiang=self.file_menu.Append(-1,u"数学降序\tCtrl-E", u"按数学成绩降序排列生成:数学降序排列.csv")
		self.Bind(wx.EVT_MENU,lambda evt, cs0=[2,'SHUXUE',1,u'数学降序排列.csv'] :self.paixu_funcs(evt,cs0),self.shuxuejiang)
		self.shuxuejiang.Enable(0)
		self.file_menu.AppendSeparator()
		
		
		self.shuxuesheng=self.file_menu.Append(-1,u"数学升序\tCtrl-F", u"按数学成绩升序排列生成:数学升序排列.csv")
		self.Bind(wx.EVT_MENU,lambda evt, cs0=[3,'SHUXUE',0,u'数学升序排列.csv'] :self.paixu_funcs(evt,cs0),self.shuxuesheng)
		self.shuxuesheng.Enable(0)
		self.file_menu.AppendSeparator()
		
		
		self.xuehaojiang=self.file_menu.Append(-1,u"学号降序\tCtrl-G", u"按学号降序排列生成:学号降序排列.csv")
		self.Bind(wx.EVT_MENU,lambda evt, cs0=[4,'NO',1,u'学号降序排列.csv'] :self.paixu_funcs(evt,cs0),self.xuehaojiang)
		self.xuehaojiang.Enable(0)
		self.file_menu.AppendSeparator()
		
		
		self.xuehaosheng=self.file_menu.Append(-1,u"学号升序\tCtrl-H", u"按学号升序排列生成:学号升序排列.csv")
		self.Bind(wx.EVT_MENU,lambda evt, cs0=[5,'NO',0,u'学号升序排列.csv'] :self.paixu_funcs(evt,cs0),self.xuehaosheng)
		self.xuehaosheng.Enable(0)
		self.file_menu.AppendSeparator()	
		
		
		self.wx_exit=self.file_menu.Append(-1,u"退出此软件系统\tCtrl-I", "Exit")
		self.Bind(wx.EVT_MENU,self.wx_exit_funcs,self.wx_exit)
		
		
		
		self.wx_menu_bar.Append(self.file_menu,u"工具")
		self.file_menu.AppendSeparator()
		
		
		
		self.help_menu=wx.Menu()
		self.about=self.help_menu.Append(-1,u"关于此软件\tCtrl-J",u"关于 Zhang Tao's CSV")
		self.Bind(wx.EVT_MENU,self.on_about,self.about)
		self.help_menu.AppendSeparator()
		self.wx_menu_bar.Append(self.help_menu,u"软件")
		
		
		self.SetMenuBar(self.wx_menu_bar)
	def create_plot_panel(self):
		self.panel = wx.Panel(self)		

		self.hebing_c=wx.Button(self.panel,-1,u"合并为c.csv",(400,350),(100,50))
		self.Bind(wx.EVT_BUTTON,self.hebing_c_funcs,self.hebing_c)
		self.ex=wx.Button(self.panel,-1,u"退出系统",(400,405),(100,50))
		self.Bind(wx.EVT_BUTTON,self.wx_exit_funcs,self.ex)
		
		self.yuwen_j=wx.Button(self.panel,-1,u"语文降序",(505,350),(100,50))
		self.Bind(wx.EVT_BUTTON,lambda evt, cs0=[0,'YUWEN',1,u'语文降序排列.csv'] :self.paixu_funcs(evt,cs0),self.yuwen_j)
		self.yuwen_j.Enable(0)
		
		self.yuwen_s=wx.Button(self.panel,-1,u"语文升序",(505,405),(100,50))
		self.Bind(wx.EVT_BUTTON,lambda evt, cs0=[1,'YUWEN',0,u'语文升序排列.csv'] :self.paixu_funcs(evt,cs0),self.yuwen_s)
		self.yuwen_s.Enable(0)
		
		self.shuxue_j=wx.Button(self.panel,-1,u"数学降序",(610,350),(100,50))
		self.Bind(wx.EVT_BUTTON,lambda evt, cs0=[2,'SHUXUE',1,u'数学降序排列.csv'] :self.paixu_funcs(evt,cs0),self.shuxue_j)
		self.shuxue_j.Enable(0)
		
		self.shuxue_s=wx.Button(self.panel,-1,u"数学升序",(610,405),(100,50))
		self.Bind(wx.EVT_BUTTON,lambda evt, cs0=[3,'SHUXUE',0,u'数学升序排列.csv'] :self.paixu_funcs(evt,cs0),self.shuxue_s)
		self.shuxue_s.Enable(0)
		
		self.xuehao_j=wx.Button(self.panel,-1,u"学号降序",(715,350),(100,50))
		self.Bind(wx.EVT_BUTTON,lambda evt, cs0=[4,'NO',1,u'学号降序排列.csv'] :self.paixu_funcs(evt,cs0),self.xuehao_j)
		self.xuehao_j.Enable(0)
		
		self.xuehao_s=wx.Button(self.panel,-1,u"学号升序",(715,405),(100,50))
		self.Bind(wx.EVT_BUTTON,lambda evt, cs0=[5,'NO',0,u'学号升序排列.csv'] :self.paixu_funcs(evt,cs0),self.xuehao_s)
		self.xuehao_s.Enable(0)
		
		self.heng_pai=wx.BoxSizer(wx.HORIZONTAL)
		flags=wx.ALIGN_CENTER|wx.ALL
		
		self.heng_pai.Add(self.hebing_c,0,border=0,flag=flags)
		self.heng_pai.Add(self.ex,0,border=0,flag=flags)
		self.heng_pai.Add(self.yuwen_j,0,border=0,flag=flags)
		self.heng_pai.Add(self.yuwen_s,0,border=0,flag=flags)
		self.heng_pai.Add(self.shuxue_j,0,border=0,flag=flags)
		self.heng_pai.Add(self.shuxue_s,0,border=0,flag=flags)
		self.heng_pai.Add(self.xuehao_j,0,border=0,flag=flags)
		self.heng_pai.Add(self.xuehao_s,0,border=0,flag=flags)
		
		self.panel.SetSizer(self.heng_pai)
		self.panel.SetBackgroundColour([0,0,147])
		self.heng_pai.Fit(self)
if __name__ == '__main__':
	app=wx.App()#wx.PySimpleApp()
	BioMCFrame().Show(True)
	app.MainLoop()