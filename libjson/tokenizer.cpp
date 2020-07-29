#include "tokenizer.h"
#include <sstream>
#include <fstream>

namespace zsbh
{
namespace json
{

Token TokenReader::ReadNull() 
{

}

Token TokenReader::ReadNumber() 
{

}

Token TokenReader::ReadBoolean() 
{

}

Token TokenReader::ReadString() 
{

}

Token TokenReader::Next() 
{
    if (!stream_) {
        return Token();
    }
    char curr;
    stream_ >> curr;
    switch(curr) {
        case '{':
        break;
        case '}':
        break;
        case '[':
        break;
        case ']':
        break;
        case ':':
        break;
        case ',':
        break;
        case '"':
        break;
        case 't':
        break;
        case 'f':
        break;
        case 'n':
        break;
    }

}

void Tokenizer::Tokenize() 
{
    Token node;
    while (node = this->reader_.Next()) 
    {
        tokens_.push_back(node);
    }
}
} // !namespace json  
} // !namespace zsbh
