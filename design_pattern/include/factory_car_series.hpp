#include "car.hpp"
#ifndef _DESIGN_PATTERN_FACTORY_METHOD_FACTORY_CAR_SERIES_HPP_
#define _DESIGN_PATTERN_FACTORY_METHOD_FACTORY_CAR_SERIES_HPP_

namespace design_pattern
{

class FactoryCarBase
{
public:
	virtual Car * CreateCar() = 0;
};

class FactoryBMW : public FactoryCarBase
{
public:
	Car * CreateCar()
	{
		return new BMW;
	}
};

class FactoryNIO : public FactoryCarBase
{
public:
	Car * CreateCar()
	{
		return new NIO;
	}
};

}

#endif //_DESIGN_PATTERN_FACTORY_METHOD_FACTORY_CAR_SERIES_HPP_
