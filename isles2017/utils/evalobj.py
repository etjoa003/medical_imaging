from utils.utils import *


class EvalObj(object):
	def __init__(self):
		super(EvalObj, self).__init__()
		self.scores = {}
		'''
		Arrange by epochs:
		self.scores = { n_epoch : {}}

		example:
		self.scores = {
			1: {
				'dice_list' : average_dice,	
			},
			2: { ... },
			3: { ... },
			...
		}

		'''
		
	def get_dice_score_at_epoch(self, epoch, dice_list):
		self.scores[epoch] = {}
		self.scores[epoch]['dice_list'] = dice_list
		# print("    dice_list mean:%s"%(str(np.mean(dice_list))))

	def get_dice_score_latest(self,dice_list):
		self.scores['latest'] = {}
		self.scores['latest']['dice_list'] = dice_list

	def save_evaluation(self, config_data, report_name='report.txt'):
		print('save_evaluation()')
		report_dir = os.path.join(config_data['working_dir'], config_data['relative_checkpoint_dir'],config_data['model_label_name'])
		report_full_path = os.path.join(report_dir,report_name)

		txt = open(report_full_path, 'w')
		print(" %5s | %s"%("epoch", "dice_score"))
		txt.write(" %5s | %s\n"%("epoch", "dice_score"))
		for epoch in self.scores:
			avg_dice_score = np.mean(self.scores[epoch]['dice_list'])
			print(" %5s | %s"%(str(epoch), str(avg_dice_score)))
			txt.write(" %5s | %s\n"%(str(epoch), str(avg_dice_score)))
		txt.close()


class CrossEntropyLossTracker(object):
	"""docstring for CrossEntropyLossTracker"""
	def __init__(self, config_data, display_every_n_minibatchs=10):
		super(CrossEntropyLossTracker, self).__init__()
		self.display_every_n_minibatchs = display_every_n_minibatchs

		model_dir = os.path.join(config_data['working_dir'], config_data['relative_checkpoint_dir'],config_data['model_label_name'])
		self.plot_fullpath = os.path.join(model_dir,config_data['model_label_name'] +"_loss_temp" + '.jpg')
		self.plot_fullpath_without_extension = os.path.join(model_dir,config_data['model_label_name'] +"_loss_")
		
		self.running_count= 0
		self.running_error = []
		self.running_loss = 0.
		self.global_count = 0
		
		self.avg_loss = []
		self.loss_var = []
		self.k_th_global_step = []

	def store_loss(self, loss):
		self.running_loss = self.running_loss + float(loss.item())
		self.running_error.append(float(loss.item()))
		self.running_count = self.running_count + 1
		self.global_count = self.global_count + 1

		if self.running_count ==  self.display_every_n_minibatchs:
			self.avg_loss.append(self.running_loss/self.display_every_n_minibatchs)
			self.loss_var.append(np.var(self.running_error)**0.5)
			self.k_th_global_step.append(self.global_count)
			self.running_count= 0
			self.running_loss = 0.
			self.running_error = []
			self.save_loss_plot()

	def save_loss_plot(self, label_tag=None):
		# print("save_loss_plot(). Plot size:%s"%(str(len(self.k_th_global_step))))
		plt.figure()
		plt.plot(self.k_th_global_step,self.avg_loss)
		y = np.array(self.avg_loss)
		er = np.array(self.loss_var) + 1e-6
		plt.fill_between(self.k_th_global_step,y-er, y+er,color='r',alpha=0.2)
		plt.title("CrossEntropyLoss")
		plt.tight_layout()
		if label_tag is not None: plt.savefig(self.plot_fullpath_without_extension + str(label_tag) + '.jpg')
		else: plt.savefig(self.plot_fullpath)
		plt.close()
	
	

		