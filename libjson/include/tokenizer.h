#ifndef _ZSBH_JSON_TOKENIZER_
#define _ZSBH_JSON_TOKENIZER_

#include <string>
#include <ostream>
#include <list>

namespace zsbh 
{
namespace json
{
enum TokenType {
    TOKEN_COMMA = 1 << 1,       //,
    TOKEN_QUOTE = 1 << 2,       //"
    TOKEN_COLON = 1 << 3,       //:
    TOKEN_BRACE_L = 1 << 4,     //{
    TOKEN_BRACE_R = 1 << 5,     //}
    TOKEN_BRACKET_L = 1 << 6,   //[
    TOKEN_BRACKET_R = 1 << 7,   //]
    TOKEN_NULL = 1 << 8,        //null
    TOKEN_NUMBER = 1 << 9,      //^[-1-9][0-9]*$
    TOKEN_BOOLEAN = 1 << 10,    //true | false
    TOKEN_STRING = 1 << 11      //^".*"$
};

struct Token {
    TokenType type_;
    std::string value_;

    operator bool() {
        return value_ == "";
    }
};

class TokenReader
{
private:
    std::istream stream_;

    Token ReadNull();
    Token ReadBoolean();
    Token ReadString();
    Token ReadNumber();
public:
    TokenReader(const std::string& text): stream_(std::ostringstream(text).rdbuf()) {}
    TokenReader(std::ostream& file): stream_(file.rdbuf()) {}
    ~TokenReader() = default;

    Token Next();
};

class Tokenizer
{
private:
    TokenReader reader_;
    std::list<Token> tokens_;
public:
    Tokenizer() = default;
    ~Tokenizer() = default;
    void Tokenize();
};

} // !namespace json
} // !namespace zsbh

#endif // !_ZSBH_JSON_TOKENIZER_