#ifndef __%UNAME%_SCENE_H__
#define __%UNAME%_SCENE_H__

#include "cocos2d.h"

class %NAME% : public cocos2d::Layer
{
public:
    static cocos2d::Scene* createScene();
    virtual bool init();
    CREATE_FUNC(%NAME%);
};

#endif // __%UNAME%_SCENE_H__
