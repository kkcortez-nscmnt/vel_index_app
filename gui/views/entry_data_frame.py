
from tkinter import ttk
from gui.controller.file_diaologs import DatFileDiolog



years = list(range(1930,2101))
month = ["%.2d" % i for i in range(1,13)]
day = ["%.2d" % i for i in range(1, 32)]
hour  = ["%.2d" % i for i in range(00,24)]
minutes = ["%.2d" % i for i in range(00,60)]
seconds = ["%.2d" % i for i in range(00,60)]
db_colmuns = ['Date Time', 'Flow rate', 'Area', 'Avarege spd', 'X spd', 'Level' ]

class EntryDataFrame(ttk.Frame, DatFileDiolog):
    def __init__(self, parent):
        super().__init__()
        
        ##### LabelFrame arquivos sl500 #####
        self.label_sl500 = ttk.LabelFrame(self, text=" Load SL500 Data ")
        self.label_sl500.place(rely=0.03, relx=0.009, height=90, width=460)

        ##### label path dos arquivos .dat #####
        self.label_sl500_dat_path = ttk.Label(self.label_sl500, relief='ridge', anchor='w')
        self.label_sl500_dat_path.place(rely=0.08, relx=0.19, height=23, width=367)
        # label path dos arquivos .vel
        self.label_sl500_vel_path = ttk.Label(self.label_sl500, relief='ridge', anchor='w')
        self.label_sl500_vel_path.place(rely=0.60, relx=0.19, height=23, width=367)
        # botão arquivo DAT
        self.btn_sl500_file = ttk.Button(self.label_sl500, padding=2, text='dat file', command=self._select_dat_file)
        self.btn_sl500_file.place(rely=0.04, relx= 0.01)
        # botão arquivo VAL
        self.btn_sl500_file = ttk.Button(self.label_sl500, padding=2, text='vel file', command=self._select_vel_file)
        self.btn_sl500_file.place(rely=0.55, relx= 0.01)

        ##### Label frame dos arquivos .mat #####
        self.label_m9 = ttk.LabelFrame(self, text=" Load M9 Data ")
        self.label_m9.place(rely=0.195, relx=0.009, height=50, width=460)
        # label path dos arquivos .vel
        self.label_m9_path = ttk.Label(self.label_m9, relief='ridge', anchor='w')
        self.label_m9_path.place(rely=0.09,relx=0.19, height=23, width=367 )
        # botão arquivo .mat
        self.btn_m9_file = ttk.Button(self.label_m9, padding=2, text='mat file',command=self._select_mat_file)
        self.btn_m9_file.place(rely=0.04,relx=0.01)

        ##### Label frame date yyy-mm-dd #####
        self.label_set_date =ttk.LabelFrame(self, text= " Set Date: Year-Month-Day ")
        self.label_set_date.place(rely=0.33, relx=0.009, height=50, width=460)
        ##### Set date combobox #####
        # year
        self.year_combobox= ttk.Combobox(self.label_set_date, values=years)
        self.year_combobox.set("Year")
        self.year_combobox.place(rely=0.09, relx=0.01)
        # month
        self.month_combobox = ttk.Combobox(self.label_set_date, values=month)
        self.month_combobox.set("Month")
        self.month_combobox.place(rely=0.09, relx=0.345)
        # day
        self.day_combobox = ttk.Combobox(self.label_set_date, values=day)
        self.day_combobox.set("Day")
        self.day_combobox.place(rely=0.09, relx=0.68)

        ##### Label frame time hh:mm:ss #####
        self.initial_label_set_time =ttk.LabelFrame(self, text= " Set Initial Time: Hour-Minutes-Seconds ")
        self.initial_label_set_time.place(rely=0.45, relx=0.009, height=50, width=460)
        ##### Set date combobox #####
        # year
        self.initial_hour_combobox= ttk.Combobox(self.initial_label_set_time, values=hour)
        self.initial_hour_combobox.set("Hour")
        self.initial_hour_combobox.place(rely=0.09, relx=0.01)
        # month
        self.initial_minute_combobox = ttk.Combobox(self.initial_label_set_time, values=minutes)
        self.initial_minute_combobox.set("Minute")
        self.initial_minute_combobox.place(rely=0.09, relx=0.345)
        # day
        self.initial_second_combobox = ttk.Combobox(self.initial_label_set_time, values=seconds)
        self.initial_second_combobox.set("Second")
        self.initial_second_combobox.place(rely=0.09, relx=0.68)

        ##### Label frame time hh:mm:ss #####
        self.final_label_set_time =ttk.LabelFrame(self, text= " Set Final Time: Hour-Minutes-Seconds ")
        self.final_label_set_time.place(rely=0.55, relx=0.009, height=50, width=460)
        ##### Set date combobox #####
        # year
        self.final_hour_combobox= ttk.Combobox(self.final_label_set_time, values=hour)
        self.final_hour_combobox.set("Hour")
        self.final_hour_combobox.place(rely=0.09, relx=0.01)
        # month
        self.final_minute_combobox = ttk.Combobox(self.final_label_set_time, values=minutes)
        self.final_minute_combobox.set("Minute")
        self.final_minute_combobox.place(rely=0.09, relx=0.345)
        # day
        self.final_second_combobox = ttk.Combobox(self.final_label_set_time, values=seconds)
        self.final_second_combobox.set("Second")
        self.final_second_combobox.place(rely=0.09, relx=0.68)

        ##### Display Frame Data #####
        self.data_base_frame = ttk.LabelFrame(self, text='Data Base Display')
        self.data_base_frame.place(rely=0.03, relx=0.47, height=600, width=670)

        ##### Display tree view #####
        self.data_base_treeview = ttk.Treeview(self.data_base_frame)
        self.data_base_treeview.place(relheight=1, relwidth=1)
        self.db_treeview_scrolly = ttk.Scrollbar(self.data_base_treeview, orient='vertical',
            command=self.data_base_treeview.yview)
        self.db_treeview_scrollx = ttk.Scrollbar(self.data_base_treeview, orient='horizontal',
            command=self.data_base_treeview.xview)
        self.data_base_treeview.configure(yscrollcommand=self.db_treeview_scrolly.set,
            xscrollcommand=self.db_treeview_scrollx.set)
        self.db_treeview_scrolly.pack(side='right', fill='y')
        self.db_treeview_scrollx.pack(side='bottom', fill='x')
    
    




        
    
        

