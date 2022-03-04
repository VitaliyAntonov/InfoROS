
from helpFilesRos.InstallingConfiguringRos import InstallingConfiguringRos
from helpFilesRos.NavigatingRosFilesystem import NavigatingRosFilesystem
from helpFilesRos.PackageRosCreate import PackageRosCreate


class RosHelpIndex:
  """ Общий индекс """

  def __init__(self):

    # 1  Установка и настройка среды ROS
    InstallingConfiguringRos.environmentVariables() # Переменные среды
    InstallingConfiguringRos.setupFiles() # Установочные файлы
    InstallingConfiguringRos.setupFilesKinetic()
    InstallingConfiguringRos.createRosWorkspaceCatkin()  # рабочее пространство ROS catkin
    InstallingConfiguringRos.catkinMakeWithPython3() 
    InstallingConfiguringRos.checkSetupBashFile() 
    InstallingConfiguringRos.checkROS_PACKAGE_PATH() # проверка переменной среды ROS_PACKAGE_PATH

    # 2  Навигация по файловой системе ROS
    NavigatingRosFilesystem.rosTutorialsPackageInstall()
    NavigatingRosFilesystem.overviewRosFileSystem()
    NavigatingRosFilesystem.instrumentsRosFilesystem()
    NavigatingRosFilesystem.usingRospack()
    NavigatingRosFilesystem.usingRoscd()
    NavigatingRosFilesystem.viewROS_PACKAGE_PATH()
    NavigatingRosFilesystem.roscdSubdirectories()
    NavigatingRosFilesystem.roscdLog()
    NavigatingRosFilesystem.usingRosls()
    NavigatingRosFilesystem.rosTab()

    # 3  Создание пакета ROS
    PackageRosCreate.catkinStructure()
    PackageRosCreate.packageCatkinWorkspace()
    PackageRosCreate.catkinPackageCreate()
    PackageRosCreate.catkin_create_pkg()
    PackageRosCreate.workspaceBuildFile()
    PackageRosCreate.addWorkspaceRos()
    PackageRosCreate.depends1()
    PackageRosCreate.dependenciesFilePackageXml()
    PackageRosCreate.indirectDependencies()
    PackageRosCreate.rospackDepends()

    
    
      


