#include "%NAME%Scene.h"

USING_NS_CC;

Scene* %NAME%::createScene()
{
    auto scene = Scene::create();
    auto layer = %NAME%::create();
    scene->addChild(layer);

    return scene;
}

bool %NAME%::init()
{
    if ( !Layer::init() )
    {
        return false;
    }
    
    return true;
}
