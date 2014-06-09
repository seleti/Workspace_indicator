import wnck
import gtk
import appindicator
import subprocess
  
def switch(response):
  #print wnck.Workspace.get_number(response)
  #wnck.Workspace.activate(response.wnckWorkspace)
  #ws  = wnck.workspace_get_screen()
  #ws_num = ws.get_number()
  print response
  screen = wnck.screen_get_default()
  wnck.Screen.force_update(screen)
  ws = wnck.Screen.get_active_workspace(screen)
  print wnck.Workspace.get_number(ws)
  ws = wnck.Screen.get_workspace(screen, response+1)
  wnck.Workspace.activate(ws)

if __name__ == "__main__":
  ind = appindicator.Indicator("Workspace-indicator", "battery-040-charging",appindicator.CATEGORY_SYSTEM_SERVICES)
  ind.set_status(appindicator.STATUS_ACTIVE)

  # create the menu and populate it 
  menu = gtk.Menu()
  command = "gsettings get org.compiz.core:/org/compiz/profiles/unity/plugins/core/"
  h_workspaces = subprocess.Popen(command+" hsize", stdout=subprocess.PIPE, stderr=None, shell=True).communicate()
  v_workspaces = subprocess.Popen(command+" vsize", stdout=subprocess.PIPE, stderr=None, shell=True).communicate()
  workspaces = int(h_workspaces[0]) * int(v_workspaces[0])
  workspace_list = []

  
  for i in range(1, workspaces+1):
    workspace_list.append(gtk.MenuItem("Workspace " + str(i)))

    menu.append(workspace_list[i-1])

    workspace_list[i-1].connect_object("activate", switch, i-1)
  
    workspace_list[i-1].show()
  
  ind.set_menu(menu)
 
  gtk.main()
  
  
    
    