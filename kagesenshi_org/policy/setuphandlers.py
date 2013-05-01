from collective.grok import gs
from kagesenshi_org.policy import MessageFactory as _

@gs.importstep(
    name=u'kagesenshi_org.policy', 
    title=_('kagesenshi_org.policy import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('kagesenshi_org.policy.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
