
# http://wiki.ros.org/ROS/Tutorials/CreatingPackage


class PackageRosCreate:
  """ использование roscreate-pkg или catkin для создания нового пакета 
  и rospack для отображения зависимостей пакетов. """

  def catkinStructure(self):
    """ Пакет должен содержать файл package.xml, представляющий информацию о пакете.

    Метапакет catkin должен иметь соответствующий шаблонный файл CMakeLists.txt.

    У каждого пакета должна быть своя папка.
    Это означает отсутствие вложенных пакетов или нескольких пакетов, 
    использующих один и тот же каталог.
    Самый простой из возможных пакетов может иметь следующую структуру:

    my_package/
    >>> CMakeLists.txt
    >>> package.xml
    """
    
  def packageCatkinWorkspace(self):
    """ рабочее пространство catkin может выглядеть так: 
    >>> workspace_folder/        -- WORKSPACE
      >>> src/                   -- SOURCE SPACE
        >>> CMakeLists.txt       -- 'Toplevel' CMake file, provided by catkin
        >>> package_1/
          >>> CMakeLists.txt     -- CMakeLists.txt file for package_1
          >>> package.xml        -- Package manifest for package_1
        >>> ...
        >>> package_n/
          >>> CMakeLists.txt     -- CMakeLists.txt file for package_n
          >>> package.xml        -- Package manifest for package_n
    """

  def catkinPackageCreate(self):
    """ перейдите в каталог исходного пространства рабочей области catkin, которую вы создали
    >>> $ cd ~/catkin_ws/src

    используйте сценарий catkin_create_pkg для создания 
    нового пакета с именем «beginner_tutorials», который зависит от std_msgs, roscpp и rospy:
    >>> $ catkin_create_pkg beginner_tutorials std_msgs rospy roscpp
    Это создаст папку beginner_tutorials , содержащую package.xml и CMakeLists.txt, частично заполненные информацией, которую вы предоставили catkin_create_pkg.
     """

  def catkin_create_pkg(self):
    """ catkin_create_pkg требует, чтобы вы дали ему package_name и, 
    возможно, список зависимостей, от которых зависит этот пакет: 
    
    >>> catkin_create_pkg <package_name> [depend1] [depend2] [depend3]

    Продвинутые функции catkin_create_pkg описаны здесь:
    http://wiki.ros.org/catkin/commands/catkin_create_pkg
    """

  def workspaceBuildFile(self):
    """ 4. Создание рабочего пространства catkin и получение установочного файла. 
    
    собрать пакеты в рабочей области catkin:
    >>> $ cd ~/catkin_ws
    >>> $ catkin_make 

    После создания рабочей области в подпапке devel создается аналогичная структура, 
    которую обычно можно найти в /opt/ros/$ROSDISTRO_NAME.
    """

  def addWorkspaceRos(self):
    """ 4. Чтобы добавить рабочую область в среду ROS, 
    необходимо получить сгенерированный установочный файл: 
    >>> $ . ~/catkin_ws/devel/setup.bash
    """

  def depends1(self):
    """ 5.1 зависимости первого порядка теперь можно просмотреть с помощью инструмента rospack:

    $ rospack depends1 beginner_tutorials
    >>>  roscpp
    >>>  rospy
    >>>  std_msgs
    """

  def dependenciesFilePackageXml(self):
    """ зависимости для пакета хранятся в файле package.xml: 
    >>>  $ roscd beginner_tutorials
    >>>  $ cat package.xml

    >>>  <package format="2">
    >>>  ...
    >>>  <buildtool_depend>catkin</buildtool_depend>
    >>>  <build_depend>roscpp</build_depend>
    >>>  <build_depend>rospy</build_depend>
    >>>  <build_depend>std_msgs</build_depend>
    >>>  ...
    >>>  </package>
    """

  def indirectDependencies(self):
    """  Во многих случаях зависимость также будет иметь свои собственные зависимости. 
    Например, rospy имеет другие зависимости.
    >>> $ rospack depends1 rospy

    >>> genpy
    >>> roscpp
    >>> rosgraph
    >>> rosgraph_msgs
    >>> roslib
    >>> std_msgs
    """

  def rospackDepends(self):
    """ 5.2 Пакет может иметь довольно много косвенных зависимостей. 
    К счастью, rospack может рекурсивно определять все вложенные зависимости. 
    >>> $ rospack depends beginner_tutorials
    """

  def customizingPackage(self):
    """ 6.1 Сгенерированный package.xml должен быть в вашем новом пакете. Настройка package.xml 
    пройдемся по новому package.xml и подправим все элементы, требующие вашего внимания.
    """

  def descriptionTag(self):
    """ 6.1.1  Сначала обновите тег описания: 
    >>>  5   <description>Пакет beginner_tutorials</description>
    """

