

class InstallingConfiguringRos:
    """1. Установка и настройка среды ROS"""

    def environmentVariables(self):
        """ проверить установку переменных среды, такие как ROS_ROOT и ROS_PACKAGE_PATH:
        
        $ printenv | grep ROS"""

    def setupFiles(self):
        """файлы setup.*sh  можно получить следующим образом:

        $ source /opt/ros/<distro>/setup.bash

        Используйте короткое имя вашего дистрибутива ROS вместо <distro>"""

    def setupFilesKinetic(self):
        """ Если вы установили ROS Kinetic, команда будет выглядеть так: 

        $ source /opt/ros/kinetic/setup.bash"""

    def createRosWorkspaceCatkin(self):
        """ Давайте создадим и построим рабочее пространство Catkin: 

        $ mkdir -p ~/catkin_ws/src

        $ cd ~/catkin_ws/

        $ catkin_make 
        
        Команда catkin_make — это удобный инструмент для работы 
        с рабочими пространствами catkin. 
        Запустив его в первый раз в вашей рабочей области, 
        он создаст ссылку CMakeLists.txt в вашей папке «src»."""

    def catkinMakeWithPython3(self):
        """ Пользователи Python 3 в ROS Melodic и более ранних версиях : 
        обратите внимание, если вы собираете ROS из исходного кода 
        для достижения совместимости с Python 3 и правильно настроили свою систему, 
        то первая команда catkin_make в чистой рабочей области catkin должна быть: 

        $ catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3
        
        Это настроит catkin_make с Python 3. 
        Затем вы можете использовать только catkin_make для последующих сборок."""

    def checkSetupBashFile(self):
        """ Кроме того, если вы посмотрите в свой текущий каталог, 
        у вас теперь должны быть папки «build» и «devel». 
        Внутри папки «devel» вы можете видеть, что теперь есть несколько файлов setup.*sh. 
        При поиске любого из этих файлов эта рабочая область будет наложена поверх вашей среды. 
        Прежде чем продолжить использовать новый файл setup.*sh:
        
        $ source devel/setup.bash """

    def checkROS_PACKAGE_PATH(self):
        """ Чтобы убедиться, что ваша рабочая область правильно перекрывается 
        сценарием установки, убедитесь, что переменная среды ROS_PACKAGE_PATH 
        включает каталог, в котором вы находитесь. 
        
        $ echo $ROS_PACKAGE_PATH 
        >>> /home/youruser/catkin_ws/src:/opt/ros/kinetic/share"""



