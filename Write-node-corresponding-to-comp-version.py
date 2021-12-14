######################################### shotname and version name #########################

def update():
    print ('\n')
    scriptName = nuke.Root().name()
    v_split = scriptName.split('/')
    print (v_split)
    
    
    scriptname_withVersion = []
    for i in v_split:
        if i.endswith('.nk'):
            scriptname_withVersion.append(i)
    shotname_withVersion = (scriptname_withVersion[0].split('.nk')[0]).split('_')
    print (shotname_withVersion)
    
    shotname = shotname_withVersion[0]
    versionname = shotname_withVersion[1]
    
    print (shotname,versionname)
    
    ######################################### write node #########################
    
    
    filename = nuke.toNode('Write1')['file'].value().split('/')
    #print (filename)
    if filename:

        (filename.insert(-1,versionname))
        final_filename =  '/'.join(filename)
        print (final_filename)
        nuke.toNode('Write1')['file'].setValue(final_filename)



nuke.addOnScriptSave(update)
