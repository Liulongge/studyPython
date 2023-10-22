# 导入logging模块
import logging
import sys
import os
# 创建一个log对象
logger = logging.getLogger(__name__)

# 默认情况下，所有消息都发送到控制台，可以通过logging.basicConfig()设置输出位置，比如一个文件。
# filename		指定日志输出目标文件的文件名，指定该设置项后日志信心就不会被输出到控制台了
# filemode		指定日志文件的打开模式，默认为'a'。需要注意的是，该选项要在filename指定时才有效
# format		指定日志格式字符串，即指定日志输出时所包含的字段信息以及它们的顺序。logging模块定义的格式字段下面会列出。
# datefmt		指定日期/时间格式。需要注意的是，该选项要在format中包含时间字段%(asctime)s时才有效
# level			指定日志器的日志级别
# stream		指定日志输出目标stream，如sys.stdout、sys.stderr以及网络stream。需要说明的是，stream和filename不能同时提供，否则会引发 ValueError异常
# style			Python 3.2中新添加的配置项。指定format格式字符串的风格，可取值为'%'、'{'和'$'，默认为'%'
# handlers		Python 3.3中新添加的配置项。该选项如果被指定，它应该是一个创建了多个Handler的可迭代对象，这些handler将会被添加到root logger。需要说明的是：filename、stream和handlers这三个配置项只能有一个存在，不能同时出现2个或3个，否则会引发ValueError异常。

# 下面是一个将所有消息输出到文件的示例：
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename = 'example.log', level = logging.DEBUG, format = LOG_FORMAT, datefmt=DATE_FORMAT)

# 日志等级:
# DEBUG		最详细的日志信息，典型应用场景是，问题诊断
# INFO	    信息详细程度仅次于DEBUG，通常只记录关键节点信息，用于确认一切都是按照我们预期的那样进行工作
# WARNING	当某些不期望的事情发生时记录的信息（如，磁盘可用空间较低），但是此时应用程序还是正常运行的
# ERROR		由于一个更严重的问题导致某些功能不能正常运行时记录的信息
# CRITICAL	当发生严重错误，导致应用程序不能继续运行时记录的信息

logger.debug('[%s %s %d]: Debugging information', os.path.basename(__file__),  __name__, sys._getframe().f_lineno)
logger.info('[%s %s %d]: Informational message', os.path.basename(__file__),  __name__, sys._getframe().f_lineno)
logger.warning('[%s %s %d]: Warning message', os.path.basename(__file__),  __name__, sys._getframe().f_lineno)
logger.error('[%s %s %d]: Error message', os.path.basename(__file__),  __name__, sys._getframe().f_lineno)
logger.critical('[%s %s %d]: Critical message', os.path.basename(__file__),  __name__, sys._getframe().f_lineno)
