#ifndef __%UPPER_NAME%_SCENE_H__
#define __%UPPER_NAME%_SCENE_H__

#include "cocos2d.h"

class %NAME% : public cocos2d::Layer
{
public:    
    static cocos2d::Scene* createScene();
    virtual bool init();
    CREATE_FUNC(%NAME%);
};

#endif // __%NAME%_SCENE_H__
