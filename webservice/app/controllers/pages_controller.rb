class PagesController < ApplicationController
  require 'base64'

  def index
  end

  def upload_picture
    image = params[:picture]

    respond_to do |format|
      if !image.nil?
        ext = image.original_filename.split('.')[-1]
        if ext == 'jpg' || ext == 'png'
          name = Time.now.to_i
          new_filename = "#{name}.#{ext}"
          File.open(Rails.root.join('public', 'pictures', new_filename), 'wb') do |file|
            file.write(image.read)
          end
          format.html { redirect_to root_path, notice: 'Picture successfully uploaded.' }
        else
          format.html { redirect_to root_path, alert: 'Picture extension invalid.' }
        end
      else
        format.html { redirect_to root_path, alert: 'First take a picture.' }
      end
    end
  end

  def upload_image
    image = params[:image]

    respond_to do |format|
      if !image.nil?
        image_data = Base64.decode64(image['data:image/png;base64,'.length .. -1])

        name = Time.now.to_i
        filename = "#{name}.jpg"

        File.open(Rails.root.join('public', 'pictures', filename), 'wb') do |file|
          file.write(image_data)
        end

        response = get_image_text(filename)

        format.json { render json: {status: 'ok', msg: 'Server got and processed image.', txt: response} }
      else
        format.json { render json: {status: 'error', msg: 'Something went wrong.'} }
      end
    end
  end
end
